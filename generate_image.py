#!/usr/bin/env python3
"""
Product Showcase Image Generator
Creates professional marketing images with brand text + tilted UI mockup.

Supports:
- Direct screenshot input (--screenshot)
- Auto-screenshot from URL (--url)
- Light or gradient backgrounds
- Customizable tilt, shadow, colors
"""

import argparse
import base64
import tempfile
import asyncio
from pathlib import Path


async def screenshot_url(url: str, width: int = 1280, height: int = 800, wait_ms: int = 1000) -> bytes:
    """Take a screenshot of a URL using Playwright."""
    from playwright.async_api import async_playwright
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": width, "height": height})
        
        await page.goto(url, wait_until='networkidle')
        if wait_ms:
            await page.wait_for_timeout(wait_ms)
        
        screenshot = await page.screenshot(type='png')
        await browser.close()
        
        return screenshot


def generate_html(
    brand: str,
    tagline: str,
    screenshot_b64: str,
    bg_color: str,
    text_color: str,
    accent: str,
    tilt: float,
    shadow: bool,
    width: int,
    height: int,
) -> str:
    """Generate HTML for the showcase layout."""
    
    shadow_css = """
        filter: drop-shadow(0 25px 50px rgba(0, 0, 0, 0.3))
                drop-shadow(0 10px 20px rgba(0, 0, 0, 0.2));
    """ if shadow else ""
    
    tagline_html = f'<div class="tagline">{tagline}</div>' if tagline else ''
    
    return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            width: {width}px;
            height: {height}px;
            background: {bg_color};
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            display: flex;
            overflow: hidden;
        }}
        
        .container {{
            display: flex;
            width: 100%;
            height: 100%;
            align-items: center;
            justify-content: space-between;
            padding: 40px 60px;
        }}
        
        .brand-side {{
            flex: 0 0 35%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding-right: 40px;
        }}
        
        .brand-name {{
            font-size: 72px;
            font-weight: 800;
            color: {text_color};
            letter-spacing: -2px;
            line-height: 1;
            margin-bottom: 16px;
        }}
        
        .tagline {{
            font-size: 24px;
            font-weight: 500;
            color: {text_color};
            opacity: 0.7;
            line-height: 1.4;
        }}
        
        .mockup-side {{
            flex: 0 0 60%;
            display: flex;
            align-items: center;
            justify-content: center;
            perspective: 1000px;
        }}
        
        .mockup-container {{
            transform: rotateY(-{tilt}deg) rotateX(2deg);
            transform-style: preserve-3d;
            {shadow_css}
        }}
        
        .mockup-image {{
            max-width: 100%;
            max-height: {height - 80}px;
            border-radius: 12px;
            border: 1px solid rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="brand-side">
            <div class="brand-name">{brand}</div>
            {tagline_html}
        </div>
        <div class="mockup-side">
            <div class="mockup-container">
                <img class="mockup-image" src="data:image/png;base64,{screenshot_b64}" />
            </div>
        </div>
    </div>
</body>
</html>'''


async def render_html_to_image(html: str, output_path: str, width: int, height: int):
    """Render HTML to PNG using Playwright."""
    from playwright.async_api import async_playwright
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": width, "height": height})
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(html)
            temp_path = f.name
        
        try:
            await page.goto(f'file://{temp_path}')
            await page.wait_for_load_state('networkidle')
            await page.screenshot(path=output_path, type='png', scale='device')
        finally:
            Path(temp_path).unlink(missing_ok=True)
            await browser.close()


async def main_async(args):
    """Async main function."""
    
    # Get screenshot bytes
    if args.url:
        print(f"Screenshotting {args.url}...")
        screenshot_bytes = await screenshot_url(
            args.url,
            width=args.viewport_width,
            height=args.viewport_height,
            wait_ms=args.wait
        )
        screenshot_b64 = base64.b64encode(screenshot_bytes).decode('utf-8')
    elif args.screenshot:
        screenshot_path = Path(args.screenshot)
        if not screenshot_path.exists():
            print(f"Error: Screenshot not found: {args.screenshot}")
            return 1
        with open(screenshot_path, 'rb') as f:
            screenshot_b64 = base64.b64encode(f.read()).decode('utf-8')
    else:
        print("Error: Provide either --screenshot or --url")
        return 1
    
    # Parse background
    if args.gradient:
        parts = [p.strip() for p in args.gradient.split(',')]
        if len(parts) != 2:
            print("Error: --gradient must be 'from,to' (e.g., '#1a1a2e,#16213e')")
            return 1
        bg_color = f"linear-gradient(135deg, {parts[0]} 0%, {parts[1]} 100%)"
        text_color = "#ffffff"
    else:
        bg_color = args.bg_color
        text_color = args.text_color
    
    # Generate HTML
    html = generate_html(
        brand=args.brand,
        tagline=args.tagline,
        screenshot_b64=screenshot_b64,
        bg_color=bg_color,
        text_color=text_color,
        accent=args.accent,
        tilt=args.tilt,
        shadow=not args.no_shadow,
        width=args.width,
        height=args.height,
    )
    
    # Render
    print(f"Generating {args.output}...")
    await render_html_to_image(html, args.output, args.width, args.height)
    print(f"Done: {args.output}")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description='Generate product showcase images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # From URL (easiest)
  %(prog)s --url https://app.example.com --brand "MyApp" -o launch.png

  # From screenshot file
  %(prog)s --screenshot app.png --brand "MyApp" -o launch.png

  # With tagline and gradient
  %(prog)s --url https://app.example.com --brand "MyApp" \\
    --tagline "Ship faster with AI" --gradient "#1a1a2e,#16213e" -o launch.png
        '''
    )
    
    # Input (one required)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--url', '-u', help='URL to screenshot')
    input_group.add_argument('--screenshot', '-s', help='Path to screenshot file')
    
    # Required
    parser.add_argument('--brand', '-b', required=True, help='Brand name')
    parser.add_argument('--output', '-o', required=True, help='Output file path')
    
    # Optional - content
    parser.add_argument('--tagline', '-t', default='', help='Tagline below brand')
    
    # Optional - styling
    parser.add_argument('--bg-color', default='#f5f5f5', help='Background color')
    parser.add_argument('--text-color', default='#111111', help='Text color')
    parser.add_argument('--gradient', help='Gradient as "from,to" (overrides bg/text colors)')
    parser.add_argument('--accent', default='#00D4AA', help='Accent color')
    parser.add_argument('--tilt', type=float, default=4, help='Tilt degrees (default: 4)')
    parser.add_argument('--no-shadow', action='store_true', help='Disable shadow')
    
    # Optional - dimensions
    parser.add_argument('--width', type=int, default=1200, help='Output width')
    parser.add_argument('--height', type=int, default=675, help='Output height')
    parser.add_argument('--viewport-width', type=int, default=1280, help='URL viewport width')
    parser.add_argument('--viewport-height', type=int, default=800, help='URL viewport height')
    parser.add_argument('--wait', type=int, default=1000, help='Wait ms after page load')
    
    args = parser.parse_args()
    return asyncio.run(main_async(args))


if __name__ == '__main__':
    exit(main())

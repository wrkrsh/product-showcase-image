#!/usr/bin/env python3
"""
Product Showcase Image Generator
Creates professional marketing images with brand text + tilted screenshot mockup.

Generic version - works with any screenshot input.
"""

import argparse
import base64
import tempfile
from pathlib import Path


def generate_html(
    brand: str,
    tagline: str,
    screenshot_b64: str,
    bg_color: str,
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
    
    return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
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
            color: #111;
            letter-spacing: -2px;
            line-height: 1;
            margin-bottom: 16px;
        }}
        
        .brand-accent {{
            color: {accent};
        }}
        
        .tagline {{
            font-size: 24px;
            font-weight: 500;
            color: #666;
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
            <div class="tagline">{tagline}</div>
        </div>
        <div class="mockup-side">
            <div class="mockup-container">
                <img class="mockup-image" src="data:image/png;base64,{screenshot_b64}" />
            </div>
        </div>
    </div>
</body>
</html>'''


def generate_gradient_html(
    brand: str,
    tagline: str,
    screenshot_b64: str,
    gradient_from: str,
    gradient_to: str,
    accent: str,
    tilt: float,
    shadow: bool,
    width: int,
    height: int,
) -> str:
    """Generate HTML with gradient background."""
    
    shadow_css = """
        filter: drop-shadow(0 25px 50px rgba(0, 0, 0, 0.4))
                drop-shadow(0 10px 20px rgba(0, 0, 0, 0.3));
    """ if shadow else ""
    
    return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            width: {width}px;
            height: {height}px;
            background: linear-gradient(135deg, {gradient_from} 0%, {gradient_to} 100%);
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
            color: #fff;
            letter-spacing: -2px;
            line-height: 1;
            margin-bottom: 16px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }}
        
        .tagline {{
            font-size: 24px;
            font-weight: 500;
            color: rgba(255,255,255,0.9);
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
            border: 1px solid rgba(255,255,255,0.2);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="brand-side">
            <div class="brand-name">{brand}</div>
            <div class="tagline">{tagline}</div>
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
        
        # Write HTML to temp file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(html)
            temp_path = f.name
        
        try:
            await page.goto(f'file://{temp_path}')
            await page.wait_for_load_state('networkidle')
            
            # Screenshot at 2x for crisp output
            await page.screenshot(
                path=output_path,
                type='png',
                scale='device',
            )
        finally:
            Path(temp_path).unlink(missing_ok=True)
            await browser.close()


def main():
    parser = argparse.ArgumentParser(
        description='Generate product showcase images from screenshots',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Basic usage with screenshot
  python generate_image.py --screenshot app.png --brand "MyApp" --output launch.png

  # With tagline and custom colors
  python generate_image.py --screenshot app.png --brand "MyApp" \\
    --tagline "Ship faster with AI" --accent "#6366f1" --output launch.png

  # Gradient background (dark mode friendly)
  python generate_image.py --screenshot app.png --brand "MyApp" \\
    --gradient "#1a1a2e,#16213e" --output launch.png

  # Adjust tilt and disable shadow
  python generate_image.py --screenshot app.png --brand "MyApp" \\
    --tilt 8 --no-shadow --output launch.png
        '''
    )
    
    parser.add_argument('--screenshot', '-s', required=True,
                        help='Path to screenshot image (PNG/JPG)')
    parser.add_argument('--brand', '-b', required=True,
                        help='Brand name (displayed large on left)')
    parser.add_argument('--tagline', '-t', default='',
                        help='Tagline text below brand name')
    parser.add_argument('--output', '-o', required=True,
                        help='Output file path')
    parser.add_argument('--bg-color', default='#f5f5f5',
                        help='Background color (default: #f5f5f5)')
    parser.add_argument('--gradient', default=None,
                        help='Gradient colors as "from,to" (overrides bg-color)')
    parser.add_argument('--accent', default='#00D4AA',
                        help='Accent color (default: #00D4AA)')
    parser.add_argument('--tilt', type=float, default=4,
                        help='Mockup tilt in degrees (default: 4)')
    parser.add_argument('--no-shadow', action='store_true',
                        help='Disable drop shadow on mockup')
    parser.add_argument('--width', type=int, default=1200,
                        help='Image width in pixels (default: 1200)')
    parser.add_argument('--height', type=int, default=675,
                        help='Image height in pixels (default: 675, Twitter optimal)')
    
    args = parser.parse_args()
    
    # Read and encode screenshot
    screenshot_path = Path(args.screenshot)
    if not screenshot_path.exists():
        print(f"Error: Screenshot not found: {args.screenshot}")
        return 1
    
    with open(screenshot_path, 'rb') as f:
        screenshot_b64 = base64.b64encode(f.read()).decode('utf-8')
    
    # Generate HTML
    if args.gradient:
        parts = args.gradient.split(',')
        if len(parts) != 2:
            print("Error: --gradient must be 'from,to' format (e.g., '#1a1a2e,#16213e')")
            return 1
        html = generate_gradient_html(
            brand=args.brand,
            tagline=args.tagline,
            screenshot_b64=screenshot_b64,
            gradient_from=parts[0].strip(),
            gradient_to=parts[1].strip(),
            accent=args.accent,
            tilt=args.tilt,
            shadow=not args.no_shadow,
            width=args.width,
            height=args.height,
        )
    else:
        html = generate_html(
            brand=args.brand,
            tagline=args.tagline,
            screenshot_b64=screenshot_b64,
            bg_color=args.bg_color,
            accent=args.accent,
            tilt=args.tilt,
            shadow=not args.no_shadow,
            width=args.width,
            height=args.height,
        )
    
    # Render to image
    import asyncio
    asyncio.run(render_html_to_image(html, args.output, args.width, args.height))
    
    print(f"Generated: {args.output}")
    return 0


if __name__ == '__main__':
    exit(main())

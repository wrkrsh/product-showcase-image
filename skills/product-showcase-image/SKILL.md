---
name: product-showcase-image
description: Generate professional product showcase images. Use when user needs marketing visuals, Twitter launch images, Product Hunt graphics, or app mockups with brand + tilted screenshot layout.
---

# Product Showcase Image Generator

Generate professional marketing images with brand name on left and tilted UI mockup on right.

## When to use
- User asks for "launch image", "Twitter thread image", "product showcase"
- User needs marketing visuals for Product Hunt, social media
- User wants a professional app mockup with branding

## How to use

The script is at the plugin root: `generate_image.py`

### From URL (auto-screenshot)
```bash
python3 generate_image.py --url https://app.example.com --brand "AppName" -o output.png
```

### From screenshot file
```bash
python3 generate_image.py --screenshot screenshot.png --brand "AppName" -o output.png
```

### With tagline and gradient background
```bash
python3 generate_image.py \
  --url https://app.example.com \
  --brand "AppName" \
  --tagline "Ship faster with AI" \
  --gradient "#1a1a2e,#16213e" \
  -o output.png
```

## Options

| Option | Description |
|--------|-------------|
| `--url` | URL to screenshot (auto) |
| `--screenshot` | Path to existing screenshot |
| `--brand` | Brand name (required) |
| `--tagline` | Tagline below brand |
| `--gradient` | Gradient bg as "from,to" |
| `--bg-color` | Solid bg color (default: #f5f5f5) |
| `--tilt` | Rotation degrees (default: 4) |
| `--no-shadow` | Disable drop shadow |
| `-o, --output` | Output file path (required) |

## Requirements

Playwright must be installed:
```bash
pip install playwright && playwright install chromium
```

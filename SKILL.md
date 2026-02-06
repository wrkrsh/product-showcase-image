---
name: product-showcase-image
description: Generate professional product showcase images. Use when user needs marketing visuals, Twitter launch images, Product Hunt graphics, or app mockups with brand + tilted screenshot layout.
---

# Product Showcase Image Generator

Generate professional marketing images with brand text on left and tilted UI mockup on right.

## When to use
- User asks for "launch image", "Twitter thread image", "product showcase"
- User needs marketing visuals for Product Hunt, social media
- User wants a professional app mockup with branding

## Quick Start

```bash
# Basic usage with URL
python3 generate_image.py --url https://app.example.com --brand "AppName" -o output.png

# With tagline and dark gradient (recommended for dark UIs)
python3 generate_image.py \
  --url https://app.example.com \
  --brand "AppName" \
  --tagline "Your catchy tagline" \
  --gradient "#0a0a0a,#1a1a2e" \
  -o output.png
```

## Key Options

| Option | Default | Description |
|--------|---------|-------------|
| `--url` | - | URL to screenshot (auto) |
| `--screenshot` | - | Path to existing screenshot |
| `--brand` | required | Brand name displayed on left |
| `--tagline` | - | Tagline below brand name |
| `--gradient` | - | Gradient bg as "from,to" (e.g., "#0a0a0a,#1a1a2e") |
| `--tilt` | 3 | 2D rotation degrees, **positive = tilt right** |
| `--width` | 1920 | Output image width |
| `--height` | 1080 | Output image height |
| `--viewport-width` | 1800 | Screenshot viewport width (higher = crispier) |
| `--viewport-height` | 1100 | Screenshot viewport height |

## Best Practices

### For crispy, edge-to-edge images:
```bash
python3 generate_image.py \
  --url "https://app.example.com" \
  --brand "Brand" \
  --tagline "tagline here" \
  --gradient "#0a0a0a,#1a1a2e" \
  --width 1920 --height 1080 \
  --viewport-width 1800 --viewport-height 1100 \
  --tilt 3 \
  -o output.png
```

### Common mistakes to avoid:
1. **Tilt direction**: Positive values tilt RIGHT, negative tilt left. Use positive (3) for standard marketing look.
2. **3D vs 2D tilt**: This tool uses 2D rotation (flat tilt), not 3D perspective rotation.
3. **Viewport size**: Use high viewport (1800x1100+) for crispy screenshots. Low viewport = blurry.
4. **Edge-to-edge**: The screenshot is scaled to 115% height to touch top/bottom edges.

### Font
Uses **Outfit** font (Google Fonts) - clean, modern, works well for tech brands.

## Requirements

```bash
pip install playwright && playwright install chromium
```

## Examples

### Dark theme app (recommended)
```bash
python3 generate_image.py \
  --url "https://app.wrkr.sh/tasks?demo=1" \
  --brand "wrkr" \
  --tagline "ai workers that actually work" \
  --gradient "#0a0a0a,#1a1a2e" \
  -o showcase.png
```

### Light theme app
```bash
python3 generate_image.py \
  --url "https://example.com" \
  --brand "Example" \
  --tagline "your tagline" \
  --bg-color "#f5f5f5" \
  --text-color "#111111" \
  -o showcase.png
```

### From existing screenshot
```bash
python3 generate_image.py \
  --screenshot ./my-screenshot.png \
  --brand "Brand" \
  --gradient "#0a0a0a,#1a1a2e" \
  -o showcase.png
```

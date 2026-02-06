---
name: product-showcase-image
description: Create professional product showcase images from any screenshot. Generates marketing visuals with brand name on left and tilted UI mockup on right. Works with any app screenshot. Triggers: "create launch image", "product showcase", "twitter thread image", "marketing visual", "app mockup".
---

# Product Showcase Image Generator

Create professional marketing images from any screenshot - brand on left, tilted mockup on right.

## Quick Start

```bash
python3 scripts/generate_image.py \
  --screenshot /path/to/your-app.png \
  --brand "YourApp" \
  --tagline "Ship faster with AI" \
  --output launch.png
```

## Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `--screenshot` | Yes | - | Path to your app screenshot (PNG/JPG) |
| `--brand` | Yes | - | Brand name (large text on left) |
| `--tagline` | No | "" | Tagline below brand name |
| `--output` | Yes | - | Output file path |
| `--bg-color` | No | #f5f5f5 | Background color |
| `--gradient` | No | - | Gradient as "from,to" (overrides bg-color) |
| `--accent` | No | #00D4AA | Accent color |
| `--tilt` | No | 4 | Mockup rotation in degrees |
| `--no-shadow` | No | false | Disable drop shadow |
| `--width` | No | 1200 | Image width (Twitter optimal) |
| `--height` | No | 675 | Image height (Twitter optimal) |

## Examples

### Basic - Light background
```bash
python3 scripts/generate_image.py \
  --screenshot dashboard.png \
  --brand "MyApp" \
  --output launch.png
```

### With tagline
```bash
python3 scripts/generate_image.py \
  --screenshot dashboard.png \
  --brand "MyApp" \
  --tagline "The future of productivity" \
  --output launch.png
```

### Gradient background (great for dark screenshots)
```bash
python3 scripts/generate_image.py \
  --screenshot dashboard.png \
  --brand "MyApp" \
  --gradient "#1a1a2e,#16213e" \
  --output launch.png
```

### Custom accent and tilt
```bash
python3 scripts/generate_image.py \
  --screenshot dashboard.png \
  --brand "MyApp" \
  --accent "#6366f1" \
  --tilt 8 \
  --output launch.png
```

### No shadow (flat design)
```bash
python3 scripts/generate_image.py \
  --screenshot dashboard.png \
  --brand "MyApp" \
  --no-shadow \
  --output launch.png
```

## Requirements

- Python 3.8+
- Playwright (`pip install playwright && playwright install chromium`)

## Output

- PNG image at 2x resolution for crisp display
- Twitter-optimized 1200x675 default dimensions
- Professional shadow and 3D tilt effect

## Tips

1. **Screenshot size**: Use high-resolution screenshots (at least 1200px wide)
2. **Dark mode apps**: Use `--gradient` for better contrast
3. **Tilt**: Lower values (2-4) look subtle, higher (6-10) more dramatic
4. **Tagline**: Keep it short - 3-6 words works best

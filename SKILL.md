---
name: product-showcase-image
description: Generate professional product showcase images from URL or screenshot. Creates marketing visuals with brand name + tilted UI mockup. Perfect for Twitter launches, Product Hunt, social media. Triggers: "create launch image", "product showcase", "twitter thread image", "marketing visual", "app mockup", "screenshot mockup".
---

# Product Showcase Image Generator

Generate professional marketing images - brand on left, tilted mockup on right.

## Quick Start

```bash
# From URL (auto-screenshot)
python3 generate_image.py --url https://app.example.com --brand "MyApp" -o launch.png

# From file
python3 generate_image.py --screenshot app.png --brand "MyApp" -o launch.png
```

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/wrkrsh/product-showcase-image/main/install.sh | bash
```

## Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `--url` | * | - | URL to screenshot |
| `--screenshot` | * | - | Path to image (alternative to --url) |
| `--brand` | Yes | - | Brand name |
| `--output` | Yes | - | Output file path |
| `--tagline` | No | "" | Tagline below brand |
| `--bg-color` | No | #f5f5f5 | Background color |
| `--gradient` | No | - | Gradient as "from,to" |
| `--tilt` | No | 4 | Rotation degrees |
| `--no-shadow` | No | - | Disable shadow |
| `--width` | No | 1200 | Output width |
| `--height` | No | 675 | Output height |
| `--viewport-width` | No | 1280 | Viewport for URL |
| `--viewport-height` | No | 800 | Viewport for URL |
| `--wait` | No | 1000 | Wait ms after page load |

\* Either `--url` or `--screenshot` required

## Examples

### Light background
```bash
python3 generate_image.py --url https://app.example.com --brand "MyApp" -o launch.png
```

### Gradient background
```bash
python3 generate_image.py --url https://app.example.com --brand "MyApp" \
  --gradient "#1a1a2e,#16213e" -o launch.png
```

### With tagline
```bash
python3 generate_image.py --url https://app.example.com --brand "MyApp" \
  --tagline "Ship faster with AI" -o launch.png
```

### From local screenshot
```bash
python3 generate_image.py --screenshot dashboard.png --brand "MyApp" -o launch.png
```

## Requirements

- Python 3.8+
- Playwright (auto-installed by install.sh)

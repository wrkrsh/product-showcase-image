# Product Showcase Image Generator

An [OpenClaw](https://openclaw.ai) skill for generating professional product showcase images from any screenshot.

Creates marketing visuals with your brand name on the left and a tilted UI mockup on the right - perfect for Twitter launch threads, Product Hunt, and social media announcements.

## Features

- Works with **any screenshot** - dashboards, landing pages, mobile apps
- Professional 3D tilt and shadow effects
- Light or gradient backgrounds
- Twitter-optimized dimensions (1200x675)
- 2x resolution for crisp display
- Customizable brand name, tagline, colors, tilt angle

## Installation

```bash
# Clone to your OpenClaw skills directory
git clone https://github.com/wrkrsh/product-showcase-image.git ~/.openclaw/workspace/skills/product-showcase-image

# Install dependencies
pip install playwright
playwright install chromium
```

## Usage

```bash
# Basic
python3 scripts/generate_image.py \
  --screenshot your-app.png \
  --brand "YourApp" \
  --output launch.png

# With tagline
python3 scripts/generate_image.py \
  --screenshot your-app.png \
  --brand "YourApp" \
  --tagline "Ship faster with AI" \
  --output launch.png

# Gradient background (for dark screenshots)
python3 scripts/generate_image.py \
  --screenshot your-app.png \
  --brand "YourApp" \
  --gradient "#1a1a2e,#16213e" \
  --output launch.png
```

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--screenshot` | required | Your app screenshot (PNG/JPG) |
| `--brand` | required | Brand name (large, left side) |
| `--tagline` | "" | Tagline below brand |
| `--output` | required | Output file path |
| `--bg-color` | #f5f5f5 | Background color |
| `--gradient` | - | Gradient as "from,to" |
| `--accent` | #00D4AA | Accent color |
| `--tilt` | 4 | Rotation degrees |
| `--no-shadow` | false | Disable shadow |

See [SKILL.md](SKILL.md) for full documentation.

## License

MIT

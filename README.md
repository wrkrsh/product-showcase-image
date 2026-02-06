# Product Showcase Image Generator

Generate professional product showcase images for Twitter launches, Product Hunt, and social media.

![Example](https://wrkr.sh/assets/images/thread-infographic.png)

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/wrkrsh/product-showcase-image/main/install.sh | bash
```

Or with pip:

```bash
pip install playwright && playwright install chromium
curl -O https://raw.githubusercontent.com/wrkrsh/product-showcase-image/main/scripts/generate_image.py
```

## Usage

### From URL (easiest)

```bash
python3 generate_image.py --url https://app.yoursite.com --brand "YourApp" -o launch.png
```

### From screenshot

```bash
python3 generate_image.py --screenshot dashboard.png --brand "YourApp" -o launch.png
```

### With tagline + gradient

```bash
python3 generate_image.py \
  --url https://app.yoursite.com \
  --brand "YourApp" \
  --tagline "Ship faster with AI" \
  --gradient "#1a1a2e,#16213e" \
  -o launch.png
```

## Options

| Option | Description |
|--------|-------------|
| `--url` | URL to screenshot |
| `--screenshot` | Or: path to image file |
| `--brand` | Brand name (required) |
| `--tagline` | Tagline below brand |
| `--gradient` | Gradient bg as "from,to" |
| `--bg-color` | Solid bg color (#f5f5f5) |
| `--tilt` | Rotation degrees (4) |
| `--no-shadow` | Disable drop shadow |

## Output

- 1200x675 (Twitter/OG optimal)
- 2x resolution for crisp display
- PNG format

## License

MIT - [wrkr](https://wrkr.sh)

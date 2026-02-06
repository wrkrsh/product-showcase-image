# Product Showcase Image

Generate professional product showcase images for launches and social media.

![Example](https://wrkr.sh/assets/images/thread-infographic.png)

## Install

One command - auto-detects your environment (Claude Code, OpenClaw, Cursor, or standalone):

```bash
curl -fsSL https://raw.githubusercontent.com/wrkrsh/product-showcase-image/main/install.sh | bash
```

### Manual install per platform

<details>
<summary><b>Claude Code</b></summary>

```bash
# Via plugin command (if in marketplace)
/plugin install wrkrsh/product-showcase-image

# Or manually
mkdir -p ~/.claude/plugins/product-showcase-image
cd ~/.claude/plugins/product-showcase-image
curl -O https://raw.githubusercontent.com/wrkrsh/product-showcase-image/main/generate_image.py
# ... copy .claude-plugin/ and skills/ from repo
```
</details>

<details>
<summary><b>OpenClaw</b></summary>

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/wrkrsh/product-showcase-image.git
```
</details>

<details>
<summary><b>Cursor / Other AI assistants</b></summary>

Just tell your AI: "Use this tool: https://github.com/wrkrsh/product-showcase-image"

Or download the script:
```bash
curl -O https://raw.githubusercontent.com/wrkrsh/product-showcase-image/main/generate_image.py
pip install playwright && playwright install chromium
```
</details>

## Usage

### From URL (auto-screenshot)
```bash
python3 generate_image.py --url https://app.yoursite.com --brand "YourApp" -o launch.png
```

### From screenshot file
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

| Option | Description | Default |
|--------|-------------|---------|
| `--url` | URL to auto-screenshot | - |
| `--screenshot` | Path to image file | - |
| `--brand` | Brand name (required) | - |
| `--tagline` | Tagline below brand | "" |
| `--gradient` | Gradient as "from,to" | - |
| `--bg-color` | Background color | #f5f5f5 |
| `--tilt` | Rotation degrees | 4 |
| `--no-shadow` | Disable shadow | false |
| `--output` | Output path (required) | - |

## Output

- 1200x675 (Twitter/OG optimal)
- 2x resolution for crisp display
- PNG format

## Platforms

Works with any AI coding assistant:
- ✅ Claude Code (via plugin)
- ✅ OpenClaw (via skill)
- ✅ Cursor (via rules or direct)
- ✅ Aider, Continue, etc. (just reference the script)
- ✅ Standalone CLI

## License

MIT - [wrkr](https://wrkr.sh)

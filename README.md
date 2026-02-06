# Product Showcase Image Generator

An [OpenClaw](https://openclaw.ai) skill for generating professional product showcase images for Twitter/social media launches.

![Example output](https://wrkr.sh/assets/images/thread-infographic.png)

## Features

- Professional marketing images with brand name + tilted UI mockup
- Twitter-optimized dimensions (1200x675)
- Customizable kanban board with tasks, agents, priorities
- 2x resolution for crisp display
- Shadow and tilt effects

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
python3 scripts/generate_image.py \
  --brand "yourapp" \
  --title "Dashboard" \
  --output launch.png
```

See [SKILL.md](SKILL.md) for full documentation and options.

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--brand` | required | Brand name (bottom left) |
| `--title` | "Dashboard" | Board title |
| `--output` | required | Output file path |
| `--accent` | #00D4AA | Accent color |
| `--tilt` | 4 | Board rotation degrees |
| `--tasks` | auto | JSON file with task data |

## License

MIT

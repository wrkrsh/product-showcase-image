---
name: product-showcase-image
description: Create professional product showcase images for Twitter/social media launches. Generates marketing visuals with brand name on left and tilted UI mockup on right. Use for launch threads, product announcements, social media graphics. Triggers: "create launch image", "product showcase", "twitter thread image", "marketing visual", "app screenshot mockup".
---

# Product Showcase Image Generator

Create professional marketing images with your product branding and a tilted UI mockup.

## Quick Start

```bash
cd /path/to/skill
python3 scripts/generate_image.py \
  --brand "yourapp" \
  --title "Marketing" \
  --output /path/to/output.png
```

## Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `--brand` | Yes | - | Brand name (bottom left) |
| `--title` | No | "Dashboard" | Workspace/board title |
| `--output` | Yes | - | Output file path |
| `--columns` | No | 5 | Number of kanban columns |
| `--tasks` | No | auto | JSON file with task data |
| `--bg-color` | No | #f5f5f5 | Background color |
| `--accent` | No | #00D4AA | Accent color (buttons, avatars) |
| `--tilt` | No | 4 | Board rotation degrees |
| `--width` | No | 1200 | Image width |
| `--height` | No | 675 | Image height (Twitter optimal) |

## Task Data Format

Create a JSON file with custom tasks:

```json
{
  "columns": ["Backlog", "Todo", "In Progress", "Review", "Done"],
  "tasks": [
    {
      "column": "Todo",
      "title": "Write blog post",
      "desc": "About AI trends...",
      "agent": "C",
      "agent_color": "blue",
      "priority": "high",
      "comments": 2,
      "status": null
    },
    {
      "column": "In Progress",
      "title": "Research competitors",
      "desc": "Top 5 analysis...",
      "agent": "R",
      "agent_color": "green",
      "priority": "high",
      "comments": 1,
      "status": "Working"
    }
  ]
}
```

### Status Values
- `null` - No status badge (backlog/todo)
- `"Working"` - Yellow/orange badge
- `"In Review"` - Orange badge
- `"Complete"` - Green badge

### Agent Colors
- `green` (#00D4AA)
- `blue` (#3b82f6)
- `purple` (#8b5cf6)
- `orange` (#f59e0b)

### Priority Values
- `high` - Red badge
- `medium` - Yellow badge
- `low` - Green badge

## Examples

### Basic usage
```bash
python3 scripts/generate_image.py --brand "myapp" --output launch.png
```

### Custom accent color
```bash
python3 scripts/generate_image.py --brand "acme" --accent "#6366f1" --output launch.png
```

### With custom tasks
```bash
python3 scripts/generate_image.py --brand "wrkr" --tasks tasks.json --output launch.png
```

## Requirements

- Python 3.8+
- Playwright (`pip install playwright && playwright install chromium`)

## Output

- PNG image at 2x resolution for crisp display
- Twitter-optimized 1200x675 default dimensions
- Professional shadow and tilt effect

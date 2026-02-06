#!/bin/bash
# Product Showcase Image Generator - Installer
# Usage: curl -fsSL https://raw.githubusercontent.com/wrkrsh/product-showcase-image/main/install.sh | bash

set -e

SKILL_DIR="${OPENCLAW_SKILLS:-$HOME/.openclaw/workspace/skills}/product-showcase-image"

echo "Installing product-showcase-image skill..."

# Create directory
mkdir -p "$SKILL_DIR"

# Download files
curl -fsSL "https://raw.githubusercontent.com/wrkrsh/product-showcase-image/main/generate_image.py" -o "$SKILL_DIR/generate_image.py"
curl -fsSL "https://raw.githubusercontent.com/wrkrsh/product-showcase-image/main/SKILL.md" -o "$SKILL_DIR/SKILL.md"

chmod +x "$SKILL_DIR/generate_image.py"

# Check for playwright
if ! python3 -c "import playwright" 2>/dev/null; then
    echo "Installing playwright..."
    pip install playwright
    playwright install chromium
fi

echo ""
echo "✓ Installed to: $SKILL_DIR"
echo ""
echo "Usage:"
echo "  python3 $SKILL_DIR/generate_image.py --url https://yourapp.com --brand \"YourApp\" -o launch.png"
echo ""

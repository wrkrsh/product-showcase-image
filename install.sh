#!/bin/bash
# Product Showcase Image - Universal Installer
# Works with: Claude Code, OpenClaw, Cursor, or standalone
#
# Usage: curl -fsSL https://raw.githubusercontent.com/wrkrsh/product-showcase-image/main/install.sh | bash

set -e

REPO="https://raw.githubusercontent.com/wrkrsh/product-showcase-image/main"
SCRIPT_NAME="generate_image.py"

# Detect environment
detect_env() {
    if command -v claude &>/dev/null; then
        echo "claude-code"
    elif [ -d "$HOME/.openclaw" ]; then
        echo "openclaw"
    elif [ -d "$HOME/.cursor" ] || [ -d ".cursor" ]; then
        echo "cursor"
    else
        echo "standalone"
    fi
}

ENV=$(detect_env)
echo "Detected environment: $ENV"

# Install based on environment
case $ENV in
    claude-code)
        # Claude Code plugin structure
        INSTALL_DIR="${HOME}/.claude/plugins/product-showcase-image"
        mkdir -p "$INSTALL_DIR/.claude-plugin"
        mkdir -p "$INSTALL_DIR/skills/product-showcase-image"
        
        # Download files
        curl -fsSL "$REPO/generate_image.py" -o "$INSTALL_DIR/generate_image.py"
        curl -fsSL "$REPO/.claude-plugin/plugin.json" -o "$INSTALL_DIR/.claude-plugin/plugin.json"
        curl -fsSL "$REPO/skills/product-showcase-image/SKILL.md" -o "$INSTALL_DIR/skills/product-showcase-image/SKILL.md"
        
        chmod +x "$INSTALL_DIR/generate_image.py"
        
        echo ""
        echo "✓ Installed Claude Code plugin to: $INSTALL_DIR"
        echo ""
        echo "Restart Claude Code, then use:"
        echo "  /product-showcase-image:generate"
        echo ""
        ;;
        
    openclaw)
        # OpenClaw skill structure
        INSTALL_DIR="${OPENCLAW_SKILLS:-$HOME/.openclaw/workspace/skills}/product-showcase-image"
        mkdir -p "$INSTALL_DIR"
        
        curl -fsSL "$REPO/generate_image.py" -o "$INSTALL_DIR/generate_image.py"
        curl -fsSL "$REPO/SKILL.md" -o "$INSTALL_DIR/SKILL.md"
        
        chmod +x "$INSTALL_DIR/generate_image.py"
        
        echo ""
        echo "✓ Installed OpenClaw skill to: $INSTALL_DIR"
        echo ""
        echo "Skill will be auto-detected. Or run directly:"
        echo "  python3 $INSTALL_DIR/generate_image.py --help"
        echo ""
        ;;
        
    cursor|standalone)
        # Standalone - just put in current dir or ~/bin
        if [ -w "." ]; then
            INSTALL_DIR="."
        else
            INSTALL_DIR="$HOME/bin"
            mkdir -p "$INSTALL_DIR"
        fi
        
        curl -fsSL "$REPO/generate_image.py" -o "$INSTALL_DIR/generate_image.py"
        curl -fsSL "$REPO/README.md" -o "$INSTALL_DIR/PRODUCT-SHOWCASE-README.md"
        
        chmod +x "$INSTALL_DIR/generate_image.py"
        
        echo ""
        echo "✓ Installed to: $INSTALL_DIR"
        echo ""
        echo "Usage:"
        echo "  python3 $INSTALL_DIR/generate_image.py --url https://yourapp.com --brand \"YourApp\" -o launch.png"
        echo ""
        ;;
esac

# Check/install playwright
if ! python3 -c "import playwright" 2>/dev/null; then
    echo "Installing playwright..."
    pip install -q playwright
    playwright install chromium
    echo "✓ Playwright installed"
fi

echo "Done!"

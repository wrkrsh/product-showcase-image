#!/usr/bin/env python3
"""
Product Showcase Image Generator
Creates professional marketing images with brand + tilted UI mockup.
"""

import argparse
import json
import tempfile
import os
from pathlib import Path

DEFAULT_TASKS = {
    "columns": ["Backlog", "Todo", "In Progress", "Review", "Done"],
    "tasks": [
        {"column": "Backlog", "title": "Create product demo video", "desc": "Short explainer for landing page...", "agent": "C", "agent_color": "blue", "priority": "medium", "comments": 0, "status": None},
        {"column": "Todo", "title": "Analyze competitor pricing", "desc": "Compare pricing tiers across competitors...", "agent": "R", "agent_color": "green", "priority": "high", "comments": 0, "status": None},
        {"column": "In Progress", "title": "Research market size data", "desc": "Gather TAM/SAM/SOM data...", "agent": "D", "agent_color": "purple", "priority": "high", "comments": 1, "status": "Working"},
        {"column": "Review", "title": "Draft investor update email", "desc": "Monthly progress update...", "agent": "E", "agent_color": "orange", "priority": "medium", "comments": 2, "status": "In Review"},
        {"column": "Done", "title": "SEO keyword analysis", "desc": "Top 50 keywords for niche...", "agent": "R", "agent_color": "green", "priority": "low", "comments": 3, "status": "Complete"},
        {"column": "Done", "title": "Q4 performance summary", "desc": None, "agent": "S", "agent_color": "green", "priority": "low", "comments": 1, "status": "Complete"},
    ]
}

AGENT_COLORS = {
    "green": "#00D4AA",
    "blue": "#3b82f6",
    "purple": "#8b5cf6",
    "orange": "#f59e0b",
}

STATUS_STYLES = {
    "Working": ("status-working", "#fef3c7", "#b45309", "#f59e0b"),
    "In Review": ("status-review", "#ffedd5", "#c2410c", "#ea580c"),
    "Complete": ("status-done", "#d1fae5", "#047857", "#10b981"),
}

PRIORITY_STYLES = {
    "high": ("#fee2e2", "#dc2626"),
    "medium": ("#fef3c7", "#d97706"),
    "low": ("#d1fae5", "#059669"),
}


def generate_html(brand: str, title: str, tasks_data: dict, accent: str, tilt: int, bg_color: str) -> str:
    """Generate the HTML for the showcase image."""
    
    columns_html = ""
    for col_name in tasks_data["columns"]:
        col_tasks = [t for t in tasks_data["tasks"] if t["column"] == col_name]
        
        # Column header
        is_actionable = col_name in ["Backlog", "Todo"]
        actions = '<span class="column-actions">+</span>' if is_actionable else ''
        
        tasks_html = ""
        for task in col_tasks:
            # Status badge
            status_html = ""
            if task.get("status"):
                style = STATUS_STYLES.get(task["status"], STATUS_STYLES["Working"])
                status_html = f'<div class="task-status" style="background:{style[1]};color:{style[2]}"><span class="status-dot" style="background:{style[3]}"></span> {task["status"]}</div>'
            
            # Description
            desc_html = f'<div class="task-desc">{task["desc"]}</div>' if task.get("desc") else ''
            
            # Agent color
            agent_color = AGENT_COLORS.get(task.get("agent_color", "green"), accent)
            
            # Priority
            priority = task.get("priority", "medium")
            pri_style = PRIORITY_STYLES.get(priority, PRIORITY_STYLES["medium"])
            
            tasks_html += f'''
                <div class="task-card">
                    {status_html}
                    <div class="task-title">{task["title"]}</div>
                    {desc_html}
                    <div class="task-footer">
                        <div class="task-left">
                            <div class="task-avatar" style="background:{agent_color}">{task.get("agent", "A")}</div>
                            <span class="task-comments">● {task.get("comments", 0)}</span>
                        </div>
                        <span class="task-priority" style="background:{pri_style[0]};color:{pri_style[1]}">{priority.title()}</span>
                    </div>
                </div>
            '''
        
        # Add task button for actionable columns
        add_btn = '<div class="add-task-btn">+ Add Task</div>' if is_actionable else ''
        
        columns_html += f'''
            <div class="column">
                <div class="column-header">
                    <div><span class="column-title">{col_name}</span><span class="column-count">{len(col_tasks)}</span></div>
                    {actions}
                </div>
                <div class="column-body">
                    {tasks_html}
                    {add_btn}
                </div>
            </div>
        '''
    
    # Get workspace icon letter
    ws_letter = title[0].upper() if title else "W"
    
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;700&family=Inter:wght@400;500;600&display=swap');
        
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            width: 1200px;
            height: 675px;
            background: {bg_color};
            font-family: 'Inter', -apple-system, sans-serif;
            position: relative;
            overflow: hidden;
        }}
        
        .brand {{
            position: absolute;
            bottom: 40px;
            left: 50px;
            font-family: 'Outfit', sans-serif;
            font-size: 52px;
            font-weight: 700;
            color: #1a1a2e;
            letter-spacing: -0.02em;
        }}
        
        .board-wrapper {{
            position: absolute;
            right: -120px;
            top: 68%;
            transform: translateY(-50%) rotate({tilt}deg);
            filter: drop-shadow(0 25px 50px rgba(0,0,0,0.15));
        }}
        
        .app-frame {{
            width: 1050px;
            background: #fff;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #e5e7eb;
        }}
        
        .topbar {{
            height: 48px;
            background: #fafafa;
            border-bottom: 1px solid #e5e7eb;
            display: flex;
            align-items: center;
            padding: 0 14px;
            gap: 6px;
        }}
        
        .topbar-logo {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding-right: 14px;
            border-right: 1px solid #e5e7eb;
            margin-right: 6px;
        }}
        
        .logo-icon {{
            width: 26px;
            height: 26px;
            background: {accent};
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 12px;
            color: #fff;
        }}
        
        .logo-text {{
            font-size: 14px;
            font-weight: 600;
            color: #1a1a2e;
        }}
        
        .workspace-btn {{
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 6px 10px;
            background: #f3f4f6;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 500;
            color: #1a1a2e;
            margin-right: 4px;
        }}
        
        .workspace-icon {{
            width: 18px;
            height: 18px;
            background: #8b5cf6;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-weight: 600;
            color: #fff;
        }}
        
        .topbar-nav {{
            display: flex;
            align-items: center;
            gap: 2px;
            flex: 1;
        }}
        
        .nav-item {{
            display: flex;
            align-items: center;
            gap: 5px;
            padding: 6px 10px;
            border-radius: 6px;
            color: #6b7280;
            font-size: 13px;
            font-weight: 500;
        }}
        
        .nav-item.active {{
            background: #e5e7eb;
            color: #1a1a2e;
        }}
        
        .topbar-right {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-left: auto;
        }}
        
        .heartbeat-btn {{
            display: flex;
            align-items: center;
            gap: 5px;
            height: 30px;
            padding: 0 10px;
            background: #f3f4f6;
            border-radius: 6px;
            font-size: 11px;
            color: #6b7280;
        }}
        
        .heartbeat-btn span {{ color: {accent}; font-weight: 600; }}
        
        .tasks-btn {{
            display: flex;
            align-items: center;
            gap: 5px;
            height: 30px;
            padding: 0 10px;
            background: #f3f4f6;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 500;
            color: #1a1a2e;
        }}
        
        .tasks-badge {{
            background: {accent};
            color: #fff;
            font-size: 10px;
            padding: 1px 6px;
            border-radius: 8px;
            font-weight: 600;
        }}
        
        .user-avatar {{
            width: 28px;
            height: 28px;
            background: #f59e0b;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            font-size: 11px;
            font-weight: 600;
        }}
        
        .heartbeat-bar {{
            height: 3px;
            background: #e5e7eb;
            position: relative;
        }}
        
        .heartbeat-fill {{
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 65%;
            background: {accent};
        }}
        
        .board {{
            display: flex;
            height: 480px;
        }}
        
        .column {{
            flex: 1;
            border-right: 1px solid #e5e7eb;
            display: flex;
            flex-direction: column;
        }}
        
        .column:last-child {{ border-right: none; }}
        
        .column-header {{
            padding: 12px 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #f3f4f6;
        }}
        
        .column-title {{
            font-size: 12px;
            font-weight: 600;
            color: #6b7280;
            text-transform: uppercase;
            letter-spacing: 0.03em;
        }}
        
        .column-count {{
            color: #9ca3af;
            font-weight: 500;
            margin-left: 6px;
        }}
        
        .column-actions {{
            font-size: 16px;
            color: #d1d5db;
        }}
        
        .column-body {{
            flex: 1;
            padding: 10px;
            overflow: hidden;
        }}
        
        .task-card {{
            background: #fafafa;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 8px;
        }}
        
        .task-status {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            font-size: 10px;
            padding: 2px 8px;
            border-radius: 10px;
            font-weight: 500;
            margin-bottom: 6px;
        }}
        
        .status-dot {{
            width: 6px;
            height: 6px;
            border-radius: 50%;
        }}
        
        .task-title {{
            font-size: 13px;
            font-weight: 500;
            color: #1a1a2e;
            margin-bottom: 4px;
            line-height: 1.3;
        }}
        
        .task-desc {{
            font-size: 11px;
            color: #6b7280;
            margin-bottom: 10px;
            line-height: 1.4;
        }}
        
        .task-footer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        
        .task-left {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .task-avatar {{
            width: 20px;
            height: 20px;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            font-size: 10px;
            font-weight: 600;
        }}
        
        .task-comments {{
            font-size: 11px;
            color: #9ca3af;
        }}
        
        .task-priority {{
            font-size: 10px;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 500;
        }}
        
        .add-task-btn {{
            padding: 8px;
            border: 1px dashed #e5e7eb;
            border-radius: 6px;
            color: #9ca3af;
            font-size: 12px;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="brand">{brand}</div>
    
    <div class="board-wrapper">
        <div class="app-frame">
            <div class="topbar">
                <div class="topbar-logo">
                    <div class="logo-icon">{brand[0].upper()}</div>
                    <span class="logo-text">{brand}</span>
                </div>
                
                <div class="workspace-btn">
                    <div class="workspace-icon">{ws_letter}</div>
                    {title} ▾
                </div>
                
                <div class="topbar-nav">
                    <div class="nav-item active">▦ Board</div>
                    <div class="nav-item">◉ Agents</div>
                    <div class="nav-item">⚙ Tools</div>
                    <div class="nav-item">◧ Knowledge</div>
                    <div class="nav-item">✦ Learnings</div>
                </div>
                
                <div class="topbar-right">
                    <div class="heartbeat-btn">♥ Next heartbeat <span>0:42</span></div>
                    <div class="tasks-btn">Tasks <span class="tasks-badge">{len(tasks_data["tasks"])}</span></div>
                    <div class="user-avatar">U</div>
                </div>
            </div>
            
            <div class="heartbeat-bar">
                <div class="heartbeat-fill"></div>
            </div>
            
            <div class="board">
                {columns_html}
            </div>
        </div>
    </div>
</body>
</html>'''
    
    return html


def generate_image(
    brand: str,
    title: str = "Dashboard",
    output: str = "showcase.png",
    tasks_file: str = None,
    bg_color: str = "#f5f5f5",
    accent: str = "#00D4AA",
    tilt: int = 4,
    width: int = 1200,
    height: int = 675,
):
    """Generate the showcase image."""
    
    # Load tasks
    if tasks_file and os.path.exists(tasks_file):
        with open(tasks_file) as f:
            tasks_data = json.load(f)
    else:
        tasks_data = DEFAULT_TASKS
    
    # Generate HTML
    html = generate_html(brand, title, tasks_data, accent, tilt, bg_color)
    
    # Write to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
        f.write(html)
        html_path = f.name
    
    try:
        # Screenshot with Playwright
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(
                viewport={'width': width, 'height': height},
                device_scale_factor=2  # 2x for crisp output
            )
            page.goto(f'file://{html_path}')
            page.wait_for_timeout(1000)  # Wait for fonts
            page.screenshot(path=output)
            browser.close()
        
        print(f"✓ Generated: {output}")
        
    finally:
        os.unlink(html_path)


def main():
    parser = argparse.ArgumentParser(description="Generate product showcase image")
    parser.add_argument("--brand", required=True, help="Brand name (bottom left)")
    parser.add_argument("--title", default="Dashboard", help="Workspace title")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--tasks", help="JSON file with task data")
    parser.add_argument("--bg-color", default="#f5f5f5", help="Background color")
    parser.add_argument("--accent", default="#00D4AA", help="Accent color")
    parser.add_argument("--tilt", type=int, default=4, help="Board tilt degrees")
    parser.add_argument("--width", type=int, default=1200, help="Image width")
    parser.add_argument("--height", type=int, default=675, help="Image height")
    
    args = parser.parse_args()
    
    generate_image(
        brand=args.brand,
        title=args.title,
        output=args.output,
        tasks_file=args.tasks,
        bg_color=args.bg_color,
        accent=args.accent,
        tilt=args.tilt,
        width=args.width,
        height=args.height,
    )


if __name__ == "__main__":
    main()

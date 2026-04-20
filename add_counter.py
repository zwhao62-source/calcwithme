# -*- coding: utf-8 -*-
"""
批量添加访客计数器到所有页面
"""
import os
import re

SITE_DIR = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"

# Counter HTML to add before </body>
COUNTER_HTML = '''
    <!-- Visitor Counter -->
    <div class="visitor-counter">
        <span>👁️ Visitors: </span>
        <span id="visitor-counter" style="display:none;">0</span>
    </div>
    <script src="js/visitor-counter.js"></script>
</body>
'''

# Counter CSS to add to style.css
COUNTER_CSS = '''
/* Visitor Counter Styles */
.visitor-counter {
    text-align: center;
    padding: 20px;
    margin-top: 40px;
    color: #666;
    font-size: 14px;
    border-top: 1px solid #eee;
}
.visitor-counter span {
    color: #007bff;
    font-weight: 600;
}
'''

def add_counter_to_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check if already has counter
    if 'visitor-counter' in content:
        return False
    
    # Add counter HTML before </body>
    if '</body>' in content:
        content = content.replace('</body>', COUNTER_HTML)
        return True
    
    return False

def add_counter_css(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check if already has counter CSS
    if 'Visitor Counter Styles' in content:
        return False
    
    # Add CSS before </style>
    if '</style>' in content:
        content = content.replace('</style>', COUNTER_CSS + '\n</style>')
        return True
    
    return False

def main():
    print("=" * 60)
    print("添加访客计数器")
    print("=" * 60)
    
    # Add counter to style.css
    style_file = os.path.join(SITE_DIR, "css", "style.css")
    if os.path.exists(style_file):
        if add_counter_css(style_file):
            with open(style_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print("[CSS] Added counter styles to style.css")
        else:
            print("[CSS] Counter styles already exist")
    
    # Add counter to all HTML files
    html_files = [f for f in os.listdir(SITE_DIR) if f.endswith('.html')]
    modified = []
    
    for filename in html_files:
        filepath = os.path.join(SITE_DIR, filename)
        try:
            if add_counter_to_file(filepath):
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                content = content.replace('</body>', COUNTER_HTML)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified.append(filename)
                print("[OK] {}".format(filename))
            else:
                print("[SKIP] {} - already has counter".format(filename))
        except Exception as e:
            print("[ERROR] {} - {}".format(filename, e))
    
    print("\n" + "=" * 60)
    print("完成！修改了 {} 个文件".format(len(modified)))
    print("=" * 60)

if __name__ == "__main__":
    main()

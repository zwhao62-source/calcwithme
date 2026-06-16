import os, re
from html.parser import HTMLParser

site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

class TE(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.skip = True
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip = False
    def handle_data(self, data):
        if not self.skip: self.text.append(data.strip())

# Blog pages
blog_dir = os.path.join(site_dir, 'blog')
if os.path.exists(blog_dir):
    blogs = sorted([f for f in os.listdir(blog_dir) if f.endswith('.html')])
    print(f'Blog pages ({len(blogs)}):')
    for b in blogs:
        path = os.path.join(blog_dir, b)
        with open(path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        ext = TE()
        ext.feed(content)
        words = len(' '.join(ext.text).split())
        print(f'  {b:55s} {words}w')

# Sample state pages
print()
sample_states = ['california', 'texas', 'florida', 'new-york']
for s in sample_states:
    path = os.path.join(site_dir, f'{s}-mortgage-calculator.html')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        ext = TE()
        ext.feed(content)
        words = len(' '.join(ext.text).split())
        title_m = re.search(r'<title>(.*?)</title>', content)
        t = title_m.group(1) if title_m else 'N/A'
        print(f'{s}: {words}w, title={t[:70]}')

# Check savings-tips.html
print()
st_path = os.path.join(site_dir, 'savings-tips.html')
with open(st_path, 'r', encoding='utf-8-sig') as f:
    content = f.read()
ext = TE()
ext.feed(content)
words = len(' '.join(ext.text).split())
print(f'savings-tips.html: {words}w')

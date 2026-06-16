import re

with open(r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site\sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

print(f'Total length: {len(content)} chars')
has_close = '</urlset>' in content
print(f'Has closing tag: {has_close}')
urls = re.findall(r'<url>', content)
print(f'Total url entries: {len(urls)}')
# Check for non-ASCII
lines = content.split('\n')
for i, line in enumerate(lines):
    if any(ord(c) > 127 for c in line):
        print(f'Line {i+1} has non-ASCII: {repr(line[:100])}')
# Print last 5 lines
print('\nLast 10 lines:')
for line in lines[-10:]:
    print(repr(line))

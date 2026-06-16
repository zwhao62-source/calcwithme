with open(r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site\sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()
lines = content.strip().split('\n')
print(f'Total lines: {len(lines)}')
print(f'First line: {lines[0]}')
print(f'Last line: {lines[-1]}')
has_close = '</urlset>' in content
print(f'Has closing tag: {has_close}')

import re
urls = re.findall(r'<loc>', content)
print(f'Total loc entries: {len(urls)}')

# Also validate with XML parser
import xml.etree.ElementTree as ET
try:
    tree = ET.parse(r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site\sitemap.xml')
    ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    root = tree.getroot()
    url_entries = root.findall(f'{ns}url')
    print(f'XML valid: YES - {len(url_entries)} URL entries parsed successfully')
except Exception as e:
    print(f'XML valid: NO - {e}')

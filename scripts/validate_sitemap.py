import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site\sitemap.xml')
root = tree.getroot()
ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
urls = root.findall(f'{ns}url')
print(f'Valid XML! {len(urls)} URL entries')
print('First 3:')
for u in urls[:3]:
    print(f'  {u.find(f"{ns}loc").text}')
print('Last 3:')
for u in urls[-3:]:
    print(f'  {u.find(f"{ns}loc").text}')

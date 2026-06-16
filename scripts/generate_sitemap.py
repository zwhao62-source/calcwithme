import os

site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

# State mortgage pages
states = [
    'alabama','alaska','arizona','arkansas','california','colorado','connecticut',
    'delaware','florida','georgia','hawaii','idaho','illinois','indiana','iowa',
    'kansas','kentucky','louisiana','maine','maryland','massachusetts','michigan',
    'minnesota','mississippi','missouri','montana','nebraska','nevada',
    'new-hampshire','new-jersey','new-mexico','new-york','north-carolina',
    'north-dakota','ohio','oklahoma','oregon','pennsylvania','rhode-island',
    'south-carolina','south-dakota','tennessee','texas','utah','vermont',
    'virginia','washington','west-virginia','wisconsin','wyoming'
]

# Canada provinces
canada = [
    'alberta','british-columbia','manitoba','new-brunswick',
    'newfoundland-labrador','nova-scotia','ontario','prince-edward-island',
    'quebec','saskatchewan'
]

lines = []
for state in states:
    fname = f'{state}-mortgage-calculator.html'
    fpath = os.path.join(site_dir, fname)
    if os.path.exists(fpath):
        lines.append(f'''  <url>
    <loc>https://calcwithme.com/{fname}</loc>
    <lastmod>2026-06-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>''')

for prov in canada:
    fname = f'{prov}-mortgage-calculator.html'
    fpath = os.path.join(site_dir, 'canada', fname)
    if os.path.exists(fpath):
        lines.append(f'''  <url>
    <loc>https://calcwithme.com/canada/{fname}</loc>
    <lastmod>2026-06-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>''')

# Blog pages
blog_dir = os.path.join(site_dir, 'blog')
if os.path.exists(blog_dir):
    for f in os.listdir(blog_dir):
        if f.endswith('.html'):
            lines.append(f'''  <url>
    <loc>https://calcwithme.com/blog/{f}</loc>
    <lastmod>2026-06-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>''')

# Append to existing sitemap
sitemap_path = os.path.join(site_dir, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before closing tag
new_entries = '\n'.join(lines)
content = content.replace('</urlset>', new_entries + '\n</urlset>')

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Sitemap updated with {len(lines)} additional URLs')

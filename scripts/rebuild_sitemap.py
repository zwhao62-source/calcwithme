import os

site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

# Main calculator pages with priorities
main_pages = [
    ('', 1.0, 'daily'),
    ('mortgage-calculator.html', 0.9, 'weekly'),
    ('car-insurance-calculator.html', 0.9, 'weekly'),
    ('parking-cost-calculator.html', 0.9, 'weekly'),
    ('auto-loan-calculator.html', 0.8, 'weekly'),
    ('gas-calculator.html', 0.8, 'weekly'),
    ('total-car-cost-calculator.html', 0.8, 'weekly'),
    ('investment-roi-calculator.html', 0.8, 'weekly'),
    ('compound-interest-calculator.html', 0.8, 'weekly'),
    ('loan-calculator.html', 0.8, 'weekly'),
    ('salary-calculator.html', 0.8, 'weekly'),
    ('retirement-calculator.html', 0.8, 'weekly'),
    ('credit-card-payoff-calculator.html', 0.8, 'weekly'),
    ('home-affordability-calculator.html', 0.8, 'weekly'),
    ('rent-vs-buy-calculator.html', 0.8, 'weekly'),
    ('tax-calculator.html', 0.8, 'weekly'),
    ('savings-goal-calculator.html', 0.7, 'weekly'),
    ('savings-tips.html', 0.7, 'weekly'),
    ('bmi-calculator.html', 0.7, 'monthly'),
    ('calorie-calculator.html', 0.7, 'monthly'),
]

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

canada_provinces = [
    'alberta','british-columbia','manitoba','new-brunswick',
    'newfoundland-labrador','nova-scotia','ontario','prince-edward-island',
    'quebec','saskatchewan'
]

lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
]

def add_url(loc, priority, changefreq):
    lines.append('  <url>')
    lines.append(f'    <loc>{loc}</loc>')
    lines.append('    <lastmod>2026-06-16</lastmod>')
    lines.append(f'    <changefreq>{changefreq}</changefreq>')
    lines.append(f'    <priority>{priority}</priority>')
    lines.append('  </url>')

# Main pages
for fname, priority, freq in main_pages:
    loc = f'https://calcwithme.com/{fname}'
    add_url(loc, priority, freq)

# State pages
for state in states:
    fname = f'{state}-mortgage-calculator.html'
    fpath = os.path.join(site_dir, fname)
    if os.path.exists(fpath):
        add_url(f'https://calcwithme.com/{fname}', '0.6', 'monthly')

# Canada pages
for prov in canada_provinces:
    fname = f'{prov}-mortgage-calculator.html'
    fpath = os.path.join(site_dir, 'canada', fname)
    if os.path.exists(fpath):
        add_url(f'https://calcwithme.com/canada/{fname}', '0.6', 'monthly')

# Blog pages
blog_dir = os.path.join(site_dir, 'blog')
if os.path.exists(blog_dir):
    for f in sorted(os.listdir(blog_dir)):
        if f.endswith('.html'):
            add_url(f'https://calcwithme.com/blog/{f}', '0.5', 'monthly')

lines.append('</urlset>')

sitemap = '\n'.join(lines)
sitemap_path = os.path.join(site_dir, 'sitemap.xml')
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap)

# Verify
url_count = sitemap.count('<url>')
has_close = '</urlset>' in sitemap
print(f'Sitemap generated: {url_count} URLs, closing tag: {has_close}')
print(f'File size: {len(sitemap)} bytes')

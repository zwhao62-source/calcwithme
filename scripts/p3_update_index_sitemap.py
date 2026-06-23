# -*- coding: utf-8 -*-
"""P3: Update index.html with new calculators, rebuild sitemap, update blog index"""
import os, re

SITE = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

# 1. Update index.html - add new calculator cards
index_path = os.path.join(SITE, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Find the Lifestyle section or add one. Let's find where to insert
# Look for a good insertion point - before the closing of calculators section
# We'll add new cards before </div> that closes the calculators grid

new_cards = '''
                    <!-- New Lifestyle Calculators -->
                    <a href="commute-cost-calculator.html" class="calc-card">
                        <span class="calc-icon">🚗</span>
                        <h3>Commute Cost Calculator</h3>
                        <p>Calculate daily, monthly & annual commuting costs. Compare driving vs transit.</p>
                        <span class="badge-new">New</span>
                    </a>
                    <a href="ev-charging-cost-calculator.html" class="calc-card">
                        <span class="calc-icon">⚡</span>
                        <h3>EV Charging Cost</h3>
                        <p>Estimate EV charging costs at home and public stations. Compare EV vs gas.</p>
                        <span class="badge-new">New</span>
                    </a>
                    <a href="cost-of-living-calculator.html" class="calc-card">
                        <span class="calc-icon">🏙️</span>
                        <h3>Cost of Living Calculator</h3>
                        <p>Compare living costs between US cities. Housing, food, transport & taxes.</p>
                        <span class="badge-new">New</span>
                    </a>
                    <a href="subscription-calculator.html" class="calc-card">
                        <span class="calc-icon">📱</span>
                        <h3>Subscription Calculator</h3>
                        <p>Add up all your subscriptions. Find hidden subscription waste.</p>
                        <span class="badge-new">New</span>
                    </a>
                    <a href="coffee-cost-calculator.html" class="calc-card">
                        <span class="calc-icon">☕</span>
                        <h3>Coffee Cost Calculator</h3>
                        <p>How much does your daily coffee cost? Compare shop vs home brewing.</p>
                        <span class="badge-new">New</span>
                    </a>
                    <a href="pet-cost-calculator.html" class="calc-card">
                        <span class="calc-icon">🐕</span>
                        <h3>Pet Cost Calculator</h3>
                        <p>True annual and lifetime cost of pet ownership. Dogs, cats & more.</p>
                        <span class="badge-new">New</span>
                    </a>
                    <a href="utility-bill-calculator.html" class="calc-card">
                        <span class="calc-icon">💡</span>
                        <h3>Utility Bill Calculator</h3>
                        <p>Estimate monthly utility costs. Electricity, gas, water, internet.</p>
                        <span class="badge-new">New</span>
                    </a>
                    <a href="wedding-budget-calculator.html" class="calc-card">
                        <span class="calc-icon">💍</span>
                        <h3>Wedding Budget Calculator</h3>
                        <p>Plan your wedding budget. Average costs by category & state.</p>
                        <span class="badge-new">New</span>
                    </a>
                    <a href="toll-calculator.html" class="calc-card">
                        <span class="calc-icon">🛣️</span>
                        <h3>Toll Cost Calculator</h3>
                        <p>Calculate daily, monthly & annual toll costs. Compare toll vs free routes.</p>
                        <span class="badge-new">New</span>
                    </a>
                    <a href="mileage-reimbursement-calculator.html" class="calc-card">
                        <span class="calc-icon">📊</span>
                        <h3>Mileage Reimbursement</h3>
                        <p>Calculate mileage at 2026 IRS rate ($0.67/mi). Business, medical, charitable.</p>
                        <span class="badge-new">New</span>
                    </a>'''

# Find insertion point - look for the last calc-card before closing div
# Try to find <!-- New Lifestyle or similar marker, or insert before the about section
if '<!-- New Lifestyle' not in index_html:
    # Find a good spot - before the about section or at end of calculators div
    # Look for pattern like </div> followed by section about
    patterns = [
        r'(<!--\s*About Section\s*-->)',
        r'(<section[^>]*id="about")',
        r'(<!--\s*about\s*-->)',
        r'(<div[^>]*class="[^"]*about)',
    ]
    inserted = False
    for pat in patterns:
        match = re.search(pat, index_html, re.IGNORECASE)
        if match:
            pos = match.start()
            index_html = index_html[:pos] + new_cards + '\n                    ' + index_html[pos:]
            inserted = True
            print(f'Inserted new cards before: {match.group()}')
            break
    
    if not inserted:
        # Try to find the last </a> in the calculators section and insert after it
        # Find all calc-card links and insert after the last one
        last_card = index_html.rfind('class="calc-card"')
        if last_card > 0:
            # Find the closing </a> after this
            close_a = index_html.find('</a>', last_card)
            if close_a > 0:
                close_a += 4
                index_html = index_html[:close_a] + '\n' + new_cards + index_html[close_a:]
                inserted = True
                print('Inserted new cards after last calc-card')
        
    if not inserted:
        print('WARNING: Could not find insertion point in index.html')
    else:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_html)
        print(f'Updated index.html (+{len(new_cards)} bytes)')

# 2. Rebuild sitemap
sitemap_path = os.path.join(SITE, 'sitemap.xml')

# Find all HTML files
html_files = []
for root, dirs, files in os.walk(SITE):
    # Skip .git, scripts, css, js, _data, blog subdirs we want to include blog
    rel = os.path.relpath(root, SITE)
    if '.git' in rel or 'scripts' in rel or 'node_modules' in rel:
        continue
    for f in files:
        if f.endswith('.html') and f != 'google-site-verification.html':
            rel_path = os.path.relpath(os.path.join(root, f), SITE).replace('\\', '/')
            html_files.append(rel_path)

html_files = sorted(set(html_files))
print(f'\nSitemap: {len(html_files)} URLs')

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for f in html_files:
    if f == 'index.html':
        url = 'https://calcwithme.com/'
        priority = '1.0'
    elif f.startswith('blog/'):
        url = 'https://calcwithme.com/' + f
        priority = '0.7'
    else:
        url = 'https://calcwithme.com/' + f.replace('.html', '.html')
        priority = '0.8'
    sitemap_xml += f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>{priority}</priority></url>\n'
sitemap_xml += '</urlset>'

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)
print(f'Sitemap written: {len(sitemap_xml)} bytes, {len(html_files)} URLs')

# 3. List new pages
new_pages = [
    'commute-cost-calculator.html',
    'ev-charging-cost-calculator.html', 
    'cost-of-living-calculator.html',
    'subscription-calculator.html',
    'coffee-cost-calculator.html',
    'pet-cost-calculator.html',
    'utility-bill-calculator.html',
    'wedding-budget-calculator.html',
    'toll-calculator.html',
    'mileage-reimbursement-calculator.html',
]
print('\nNew pages created:')
for p in new_pages:
    full = os.path.join(SITE, p)
    if os.path.exists(full):
        sz = os.path.getsize(full)
        print(f'  ✓ {p} ({sz} bytes)')
    else:
        print(f'  ✗ {p} MISSING')

print('\nDone! Ready for git commit and push.')

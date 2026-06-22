import os, re

SITE_DIR = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"

# Pages needing breadcrumb
state_pages = [
    'alabama-mortgage-calculator.html', 'alaska-mortgage-calculator.html',
    'arizona-mortgage-calculator.html', 'arkansas-mortgage-calculator.html',
    'california-mortgage-calculator.html', 'colorado-mortgage-calculator.html',
    'connecticut-mortgage-calculator.html', 'delaware-mortgage-calculator.html',
    'florida-mortgage-calculator.html', 'georgia-mortgage-calculator.html',
    'hawaii-mortgage-calculator.html', 'idaho-mortgage-calculator.html',
    'illinois-mortgage-calculator.html', 'indiana-mortgage-calculator.html',
    'iowa-mortgage-calculator.html', 'kansas-mortgage-calculator.html',
    'kentucky-mortgage-calculator.html', 'louisiana-mortgage-calculator.html',
    'maine-mortgage-calculator.html', 'maryland-mortgage-calculator.html',
    'massachusetts-mortgage-calculator.html', 'michigan-mortgage-calculator.html',
    'minnesota-mortgage-calculator.html', 'mississippi-mortgage-calculator.html',
    'missouri-mortgage-calculator.html', 'montana-mortgage-calculator.html',
    'nebraska-mortgage-calculator.html', 'nevada-mortgage-calculator.html',
    'new-hampshire-mortgage-calculator.html', 'new-jersey-mortgage-calculator.html',
    'new-mexico-mortgage-calculator.html', 'new-york-mortgage-calculator.html',
    'north-carolina-mortgage-calculator.html', 'north-dakota-mortgage-calculator.html',
    'ohio-mortgage-calculator.html', 'oklahoma-mortgage-calculator.html',
    'oregon-mortgage-calculator.html', 'pennsylvania-mortgage-calculator.html',
    'rhode-island-mortgage-calculator.html', 'south-carolina-mortgage-calculator.html',
    'south-dakota-mortgage-calculator.html', 'tennessee-mortgage-calculator.html',
    'texas-mortgage-calculator.html', 'utah-mortgage-calculator.html',
    'vermont-mortgage-calculator.html', 'virginia-mortgage-calculator.html',
    'washington-mortgage-calculator.html', 'west-virginia-mortgage-calculator.html',
    'wisconsin-mortgage-calculator.html', 'wyoming-mortgage-calculator.html',
]

# Non-state pages needing breadcrumb: (filename, category_anchor, category_name, page_name)
other_pages = [
    ('grade-calculator.html', '#other-tools', 'Tools', 'Grade Calculator'),
    ('heart-rate-calculator.html', '#health-fitness', 'Health', 'Heart Rate Zone Calculator'),
    ('hours-calculator.html', '#other-tools', 'Tools', 'Hours Calculator'),
    ('ideal-weight-calculator.html', '#health-fitness', 'Health', 'Ideal Weight Calculator'),
    ('macro-calculator.html', '#health-fitness', 'Health', 'Macro Calculator'),
    ('overtime-calculator.html', '#other-tools', 'Tools', 'Overtime Calculator'),
    ('pace-calculator.html', '#health-fitness', 'Health', 'Pace Calculator'),
    ('pregnancy-calculator.html', '#health-fitness', 'Health', 'Pregnancy Calculator'),
    ('square-footage-calculator.html', '#other-tools', 'Tools', 'Square Footage Calculator'),
    ('water-calculator.html', '#health-fitness', 'Health', 'Water Intake Calculator'),
]

state_names = {
    'alabama':'Alabama','alaska':'Alaska','arizona':'Arizona','arkansas':'Arkansas',
    'california':'California','colorado':'Colorado','connecticut':'Connecticut',
    'delaware':'Delaware','florida':'Florida','georgia':'Georgia','hawaii':'Hawaii',
    'idaho':'Idaho','illinois':'Illinois','indiana':'Indiana','iowa':'Iowa',
    'kansas':'Kansas','kentucky':'Kentucky','louisiana':'Louisiana','maine':'Maine',
    'maryland':'Maryland','massachusetts':'Massachusetts','michigan':'Michigan',
    'minnesota':'Minnesota','mississippi':'Mississippi','missouri':'Missouri',
    'montana':'Montana','nebraska':'Nebraska','nevada':'Nevada',
    'new-hampshire':'New Hampshire','new-jersey':'New Jersey','new-mexico':'New Mexico',
    'new-york':'New York','north-carolina':'North Carolina','north-dakota':'North Dakota',
    'ohio':'Ohio','oklahoma':'Oklahoma','oregon':'Oregon','pennsylvania':'Pennsylvania',
    'rhode-island':'Rhode Island','south-carolina':'South Carolina',
    'south-dakota':'South Dakota','tennessee':'Tennessee','texas':'Texas','utah':'Utah',
    'vermont':'Vermont','virginia':'Virginia','washington':'Washington',
    'west-virginia':'West Virginia','wisconsin':'Wisconsin','wyoming':'Wyoming',
}

def make_breadcrumb(name, cat_anchor, cat_name, page_name, url):
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://calcwithme.com"}},{{"@type":"ListItem","position":2,"name":"{cat_name}","item":"https://calcwithme.com/{cat_anchor}"}},{{"@type":"ListItem","position":3,"name":"{page_name}","item":"https://calcwithme.com/{url}"}}]}}</script>'

count = 0
errors = []

# Process state pages
for fname in state_pages:
    fpath = os.path.join(SITE_DIR, fname)
    if not os.path.exists(fpath):
        errors.append(f"NOT FOUND: {fname}")
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'BreadcrumbList' in content:
        continue
    state_key = fname.replace('-mortgage-calculator.html', '')
    state_name = state_names.get(state_key, state_key.title())
    page_name = f"{state_name} Mortgage Calculator"
    breadcrumb = make_breadcrumb(state_name, '#home-mortgage', 'Financial', page_name, fname)
    # Insert before </head>
    content = content.replace('</head>', breadcrumb + '\n</head>')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1

# Process other pages
for fname, cat_anchor, cat_name, page_name in other_pages:
    fpath = os.path.join(SITE_DIR, fname)
    if not os.path.exists(fpath):
        errors.append(f"NOT FOUND: {fname}")
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'BreadcrumbList' in content:
        continue
    breadcrumb = make_breadcrumb(page_name, cat_anchor, cat_name, page_name, fname)
    content = content.replace('</head>', breadcrumb + '\n</head>')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1

print(f"Added breadcrumbs to {count} pages")
if errors:
    print("Errors:", errors)

# -*- coding: utf-8 -*-
import os, re

SITE_DIR = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"

# All calculator HTML pages (exclude blog, css, js, etc.)
all_files = sorted(os.listdir(SITE_DIR))
calc_files = [f for f in all_files if f.endswith('.html') and not f.startswith('blog') and f not in ['sitemap.html', 'savings-tips.html']]

print(f"Total calculator pages: {len(calc_files)}")
print()

issues = []

for p in calc_files:
    f = os.path.join(SITE_DIR, p)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # Title check
    t = re.search(r'<title>([^<]+)</title>', c, re.I)
    title = t.group(1).strip() if t else "NO TITLE"
    has_brand = "CalcWithMe" in title
    
    # FAQ Schema check
    has_faq_schema = '"FAQPage"' in c or '"@type": "Question"' in c
    
    # FAQ HTML check
    has_faq_html = ('faq-section' in c.lower() or 'faq-item' in c.lower() or 
                   '<details' in c or ('frequently asked' in c.lower() and 'question' in c.lower()))
    
    page_issues = []
    if not has_brand:
        page_issues.append("NO_BRAND")
    if not has_faq_schema:
        page_issues.append("NO_FAQ_SCHEMA")
    if not has_faq_html:
        page_issues.append("NO_FAQ_HTML")
    
    if page_issues:
        issues.append((p, title, page_issues))
        print(f"ISSUE: {p}")
        print(f"  Title: {title[:70]}")
        print(f"  Issues: {page_issues}")
        print()
    else:
        print(f"OK: {p}")

print()
print(f"Total with issues: {len(issues)}")

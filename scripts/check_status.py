# -*- coding: utf-8 -*-
import os, re, glob

SITE_DIR = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"

pages = [
    'mortgage-calculator.html',
    'loan-calculator.html', 
    'auto-loan-calculator.html',
    'compound-interest-calculator.html',
    'credit-card-payoff-calculator.html',
    'investment-roi-calculator.html',
    'retirement-calculator.html',
    'rent-vs-buy-calculator.html',
    'salary-calculator.html',
    'savings-goal-calculator.html',
]

for p in pages:
    f = os.path.join(SITE_DIR, p)
    if not os.path.exists(f):
        print(f"MISSING: {p}")
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    t = re.search(r'<title>([^<]+)</title>', c, re.I)
    title = t.group(1).strip() if t else "NO TITLE"
    
    brand = "CalcWithMe" in title
    faq_schema = "faqpage" in c.lower() or ("schema.org" in c and "faq" in c.lower())
    howto = "how to use" in c.lower() or "how to calculate" in c.lower()
    related = "related calc" in c.lower() or "related-calc" in c.lower()
    
    issues = []
    if not brand: issues.append("NO_BRAND")
    if not faq_schema: issues.append("NO_FAQ_SCHEMA")
    if not howto: issues.append("NO_HOWTO")
    if not related: issues.append("NO_RELATED")
    
    if issues:
        print(f"{p}: {title[:50]}")
        print(f"  ISSUES: {issues}")

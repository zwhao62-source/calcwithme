# -*- coding: utf-8 -*-
import os, re

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
    has_content = len(c) > 5000
    
    # More flexible checks
    has_how = "how" in c.lower() and ("use" in c.lower() or "works" in c.lower() or "calculate" in c.lower())
    has_related = "related" in c.lower() and "calc" in c.lower()
    
    issues = []
    if not brand: issues.append("NO_BRAND")
    if not has_content: issues.append("TOO_SHORT")
    if not has_how: issues.append("NO_HOW_SECTION")
    if not has_related: issues.append("NO_RELATED")
    
    if issues:
        print(f"{p}: {title[:60]}")
        print(f"  {issues}")
    else:
        print(f"{p}: OK")

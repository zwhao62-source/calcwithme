import os, re

SITE_DIR = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"

calcs = [
    'mortgage-calculator.html',
    'loan-calculator.html',
    'auto-loan-calculator.html',
    'compound-interest-calculator.html',
]

for p in calcs:
    f = os.path.join(SITE_DIR, p)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    has_faq = '"FAQPage"' in c or '"@type": "Question"' in c
    print(f"{p}: FAQ_Schema={has_faq}")
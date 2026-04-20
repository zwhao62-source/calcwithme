# -*- coding: utf-8 -*-
"""
综合检查所有计算器页面状态：标题格式、FAQ、How to Use、Related Calculators
"""
import os
import re
import glob

SITE_DIR = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"

# 主要计算器页面（非州级）
MAIN_CALCULATORS = [
    "mortgage-calculator.html",
    "loan-calculator.html",
    "auto-loan-calculator.html",
    "compound-interest-calculator.html",
    "credit-card-payoff-calculator.html",
    "investment-roi-calculator.html",
    "retirement-calculator.html",
    "rent-vs-buy-calculator.html",
    "salary-calculator.html",
    "savings-goal-calculator.html",
]

def check_file(filepath, filename):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read().lower()
    
    title_match = re.search(r'<title>([^<]+)</title>', content, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else 'NO TITLE'
    
    return {
        'title': title,
        'has_calcwithme_brand': 'calcwithme' in title,
        'has_faq': 'faq' in content or 'frequently asked' in content,
        'has_faq_schema': 'faqpage' in content,
        'has_howto': 'how to use' in content or 'how to calculate' in content,
        'has_related': 'related calculators' in content or 'related-calc' in content,
        'has_details_faq': '<details' in content,
    }

print("=" * 80)
print("CalcWithMe 页面状态检查")
print("=" * 80)

print("\n--- 主要计算器页面 ---")
for filename in MAIN_CALCULATORS:
    filepath = os.path.join(SITE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"\n[MISSING] {filename}")
        continue
    
    info = check_file(filepath, filename)
    
    print(f"\n{filename}")
    print(f"  Title: {info['title'][:80]}")
    
    checks = []
    if info['has_calcwithme_brand']:
        checks.append('✅ Brand in title')
    else:
        checks.append('❌ NO brand in title')
    
    if info['has_faq_schema']:
        checks.append('✅ FAQ Schema')
    elif info['has_faq']:
        checks.append('⚠️ FAQ content (no schema)')
    else:
        checks.append('❌ No FAQ')
    
    if info['has_howto']:
        checks.append('✅ How to Use')
    else:
        checks.append('❌ No How to Use')
    
    if info['has_related']:
        checks.append('✅ Related Calcs')
    else:
        checks.append('❌ No Related Calcs')
    
    for c in checks:
        print(f"  {c}")

# Check a few state pages
print("\n\n--- 州级页面抽样 (5个) ---")
state_files = sorted(glob.glob(os.path.join(SITE_DIR, "*-mortgage-calculator.html")))
import random
sample = random.sample(state_files, min(5, len(state_files)))
for filepath in sample:
    filename = os.path.basename(filepath)
    info = check_file(filepath, filename)
    print(f"\n{filename}")
    print(f"  Title: {info['title'][:80]}")
    print(f"  FAQ Schema: {'✅' if info['has_faq_schema'] else '❌'}")
    print(f"  How to Use: {'✅' if info['has_howto'] else '❌'}")
    print(f"  Related Calcs: {'✅' if info['has_related'] else '❌'}")

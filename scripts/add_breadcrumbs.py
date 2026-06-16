import os, re

site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

# Map filenames to breadcrumb name
pages = {
    'car-insurance-calculator.html': 'Car Insurance Calculator',
    'gas-calculator.html': 'Gas Cost Calculator',
    'total-car-cost-calculator.html': 'Total Car Cost Calculator',
    'investment-roi-calculator.html': 'Investment ROI Calculator',
    'salary-calculator.html': 'Salary Calculator',
    'mortgage-calculator.html': 'Mortgage Calculator',
    'auto-loan-calculator.html': 'Auto Loan Calculator',
    'loan-calculator.html': 'Loan Calculator',
    'compound-interest-calculator.html': 'Compound Interest Calculator',
    'retirement-calculator.html': 'Retirement Calculator',
    'credit-card-payoff-calculator.html': 'Credit Card Payoff Calculator',
    'home-affordability-calculator.html': 'Home Affordability Calculator',
    'rent-vs-buy-calculator.html': 'Rent vs Buy Calculator',
    'savings-goal-calculator.html': 'Savings Goal Calculator',
    'tax-calculator.html': 'Tax Calculator',
    'bmi-calculator.html': 'BMI Calculator',
    'calorie-calculator.html': 'Calorie Calculator',
}

count = 0
for fname, name in pages.items():
    fpath = os.path.join(site_dir, fname)
    if not os.path.exists(fpath):
        continue
    
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Skip if already has BreadcrumbList
    if 'BreadcrumbList' in content:
        continue
    
    breadcrumb = f'''<script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calcwithme.com/"}},
        {{"@type": "ListItem", "position": 2, "name": "Calculators", "item": "https://calcwithme.com/#calculators"}},
        {{"@type": "ListItem", "position": 3, "name": "{name}", "item": "https://calcwithme.com/{fname}"}}
      ]
    }}
    </script>'''
    
    # Insert before </head>
    content = content.replace('</head>', breadcrumb + '\n</head>')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1

print(f'Added BreadcrumbList to {count} pages')

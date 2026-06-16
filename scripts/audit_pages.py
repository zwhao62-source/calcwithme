import os, re
from html.parser import HTMLParser

site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip = True
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = False
    def handle_data(self, data):
        if not self.skip:
            self.text.append(data.strip())

# Key pages to check
key_files = [
    'index.html',
    'mortgage-calculator.html',
    'car-insurance-calculator.html',
    'parking-cost-calculator.html',
    'auto-loan-calculator.html',
    'gas-calculator.html',
    'total-car-cost-calculator.html',
    'investment-roi-calculator.html',
    'compound-interest-calculator.html',
    'loan-calculator.html',
    'salary-calculator.html',
    'retirement-calculator.html',
    'credit-card-payoff-calculator.html',
    'home-affordability-calculator.html',
    'rent-vs-buy-calculator.html',
    'tax-calculator.html',
    'savings-goal-calculator.html',
    'savings-tips.html',
    'bmi-calculator.html',
    'calorie-calculator.html',
]

results = []
for f in sorted(key_files):
    path = os.path.join(site_dir, f)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8-sig') as fh:
        content = fh.read()
    
    # Word count
    ext = TextExtractor()
    ext.feed(content)
    words = len(' '.join(ext.text).split())
    
    # Title tag
    title_m = re.search(r'<title>(.*?)</title>', content)
    title = title_m.group(1) if title_m else 'NO TITLE'
    
    # Has FAQ
    has_faq = 'FAQPage' in content or 'faq-item' in content
    # Has breadcrumb
    has_breadcrumb = 'BreadcrumbList' in content
    # Has 2026
    has_2026 = '2026' in content
    # Has h2
    h2s = re.findall(r'<h2>(.*?)</h2>', content)
    
    issues = []
    if words < 600:
        issues.append(f'short({words}w)')
    if not has_faq:
        issues.append('no-FAQ')
    if not has_breadcrumb:
        issues.append('no-breadcrumb')
    if not has_2026:
        issues.append('no-2026')
    if len(h2s) < 3:
        issues.append(f'few-h2({len(h2s)})')
    
    status = ' '.join(issues) if issues else 'OK'
    print(f'{f:45s} {words:5d}w | {status}')

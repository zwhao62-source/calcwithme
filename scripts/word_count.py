import os, re

site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

pages = [
    'salary-calculator.html',
    'credit-card-payoff-calculator.html',
    'rent-vs-buy-calculator.html',
    'compound-interest-calculator.html',
    'retirement-calculator.html',
    'auto-loan-calculator.html',
    'savings-goal-calculator.html',
    'loan-calculator.html',
    'savings-tips.html',
]

print(f'{"Page":<42} {"Words":>6} {"H2s":>4} {"Title":>10}')
print('-' * 70)

for f in pages:
    path = os.path.join(site_dir, f)
    with open(path, 'r', encoding='utf-8-sig') as fh:
        content = fh.read()
    
    # Extract visible text (between body tags, strip HTML)
    body = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
    if body:
        text = body.group(1)
        text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'&[a-zA-Z]+;', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        words = len(text.split())
    else:
        words = 0
    
    h2s = len(re.findall(r'<h2>', content))
    
    title_m = re.search(r'<title>(.*?)</title>', content)
    title = title_m.group(1)[:50] if title_m else 'N/A'
    
    print(f'{f:<42} {words:>6} {h2s:>4}  {title}')

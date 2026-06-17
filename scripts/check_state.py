import os, re
site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'
f = os.path.join(site_dir, 'texas-mortgage-calculator.html')
with open(f, 'r', encoding='utf-8-sig') as fh:
    content = fh.read()
h1 = re.search(r'<h1>(.*?)</h1>', content)
h2s = re.findall(r'<h2>(.*?)</h2>', content)
body = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
text = body.group(1) if body else ''
text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', ' ', text)
text = re.sub(r'\s+', ' ', text).strip()
words = len(text.split())
print('H1:', h1.group(1) if h1 else 'N/A')
print('Words:', words)
print('H2s:')
for h in h2s:
    print('  -', h[:80])
print()
# Also check florida
f2 = os.path.join(site_dir, 'florida-mortgage-calculator.html')
with open(f2, 'r', encoding='utf-8-sig') as fh:
    c2 = fh.read()
h2s2 = re.findall(r'<h2>(.*?)</h2>', c2)
print('Florida H2s:')
for h in h2s2:
    print('  -', h[:80])

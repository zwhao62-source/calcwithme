import os, re

site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

# Update meta descriptions by regex
desc_updates = {
    'auto-loan-calculator.html': 'Free auto loan calculator 2026. Estimate monthly car payments, total interest, and compare new vs used car loans with current rates. Updated June 2026.',
    'savings-goal-calculator.html': 'Free savings goal calculator 2026. Plan how much to save monthly to reach your financial goal. Updated June 2026.',
    'loan-calculator.html': 'Free loan calculator 2026. Estimate monthly payments, total interest, and amortization for personal, student, and business loans. Updated June 2026.',
}

for f, new_desc in desc_updates.items():
    path = os.path.join(site_dir, f)
    with open(path, 'r', encoding='utf-8-sig') as fh:
        content = fh.read()
    pattern = r'<meta name="description" content="[^"]*">'
    replacement = f'<meta name="description" content="{new_desc}">'
    new_content, count = re.subn(pattern, replacement, content, count=1)
    if count > 0:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        print(f'{f}: description updated')
    else:
        print(f'{f}: no match found')

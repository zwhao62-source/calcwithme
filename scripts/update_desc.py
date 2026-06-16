import os, re

site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'
updates = {
    'auto-loan-calculator.html': (
        'Free auto loan calculator to estimate your monthly car payment',
        'Free auto loan calculator 2026. Estimate your monthly car payment with current rates. Compare new vs used car loans. Updated June 2026.'
    ),
    'savings-goal-calculator.html': (
        'Free savings goal calculator to determine how much you need to save each month',
        'Free savings goal calculator 2026. Determine how much you need to save each month to reach your goal. Updated June 2026.'
    ),
    'loan-calculator.html': (
        'Free loan calculator to estimate your monthly payment',
        'Free loan calculator 2026. Estimate your monthly payment for personal, student, and business loans. Updated June 2026.'
    ),
}
for f, (old_d, new_d) in updates.items():
    path = os.path.join(site_dir, f)
    with open(path, 'r', encoding='utf-8-sig') as fh:
        content = fh.read()
    if old_d in content:
        content = content.replace(old_d, new_d, 1)
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f'{f}: description updated')
    else:
        m = re.search(r'<meta name="description" content="([^"]*)"', content)
        print(f'{f}: old not found. Current: {m.group(1)[:80] if m else "N/A"}')

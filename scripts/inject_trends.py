import json, os, re

site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

with open(os.path.join(site_dir, 'scripts', 'state_data.json'), 'r') as f:
    data = json.load(f)

home_prices = data['home_prices']
rent_prices = data['rent_prices']
state_names = data['state_names']
years = data['years']

def make_svg_chart(values, labels, color, prefix='$', suffix='', chart_id='chart'):
    """Generate a responsive SVG line chart."""
    if not values or len(values) < 2:
        return ''
    
    w, h = 600, 220
    pad_l, pad_r, pad_t, pad_b = 55, 20, 25, 35
    chart_w = w - pad_l - pad_r
    chart_h = h - pad_t - pad_b
    
    vmin, vmax = min(values), max(values)
    vrange = vmax - vmin if vmax > vmin else 1
    
    # Calculate points
    points = []
    for i, v in enumerate(values):
        x = pad_l + (i / (len(values) - 1)) * chart_w
        y = pad_t + chart_h - ((v - vmin) / vrange) * chart_h
        points.append((x, y, v))
    
    # Y-axis labels (3 ticks)
    y_ticks = []
    for frac in [0, 0.5, 1]:
        val = vmin + frac * vrange
        y = pad_t + chart_h - frac * chart_h
        if prefix == '$' and val >= 1000:
            label = f'${int(val):,}'
        elif prefix == '$':
            label = f'${int(val)}'
        else:
            label = f'{val:.0f}{suffix}'
        y_ticks.append((y, label))
    
    # Build SVG
    svg_parts = []
    svg_parts.append(f'<svg viewBox="0 0 {w} {h}" style="width:100%;max-width:600px;height:auto;font-family:system-ui,-apple-system,sans-serif;" aria-label="Chart showing trend from {labels[0]} to {labels[-1]}">')
    
    # Grid lines
    for y, _ in y_ticks:
        svg_parts.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{w-pad_r}" y2="{y:.1f}" stroke="#e5e7eb" stroke-width="1"/>')
    
    # Area fill
    area_path = f'M {points[0][0]:.1f},{points[0][1]:.1f}'
    for x, y, v in points[1:]:
        area_path += f' L {x:.1f},{y:.1f}'
    area_path += f' L {points[-1][0]:.1f},{pad_t+chart_h} L {points[0][0]:.1f},{pad_t+chart_h} Z'
    svg_parts.append(f'<path d="{area_path}" fill="{color}15"/>')
    
    # Line
    line_path = f'M {points[0][0]:.1f},{points[0][1]:.1f}'
    for x, y, v in points[1:]:
        line_path += f' L {x:.1f},{y:.1f}'
    svg_parts.append(f'<path d="{line_path}" fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
    
    # Dots and values
    for i, (x, y, v) in enumerate(points):
        svg_parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}" stroke="white" stroke-width="2"/>')
        if prefix == '$' and v >= 1000:
            vlabel = f'${int(v):,}'
        elif prefix == '$':
            vlabel = f'${int(v)}K'
        else:
            vlabel = f'{v:.0f}{suffix}'
        # Show first, last, and peak values
        if i == 0 or i == len(points)-1 or v == vmax:
            svg_parts.append(f'<text x="{x:.1f}" y="{y-10:.1f}" text-anchor="middle" font-size="11" font-weight="600" fill="{color}">{vlabel}</text>')
    
    # Y-axis labels
    for y, label in y_ticks:
        svg_parts.append(f'<text x="{pad_l-5}" y="{y+4:.1f}" text-anchor="end" font-size="11" fill="#6b7280">{label}</text>')
    
    # X-axis labels
    for i, label in enumerate(labels):
        x = pad_l + (i / (len(labels) - 1)) * chart_w
        svg_parts.append(f'<text x="{x:.1f}" y="{h-8}" text-anchor="middle" font-size="11" fill="#6b7280">{label}</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def make_trend_section(state_key):
    """Generate the full trend section HTML for a state page."""
    name = state_names.get(state_key, state_key.title())
    hp = home_prices.get(state_key, [])
    rp = rent_prices.get(state_key, [])
    
    if not hp or not rp:
        return ''
    
    # Calculate changes
    hp_5yr = ((hp[-1] - hp[0]) / hp[0] * 100) if hp[0] > 0 else 0
    hp_1yr = ((hp[-1] - hp[-2]) / hp[-2] * 100) if hp[-2] > 0 else 0
    rp_5yr = ((rp[-1] - rp[0]) / rp[0] * 100) if rp[0] > 0 else 0
    rp_1yr = ((rp[-1] - rp[-2]) / rp[-2] * 100) if rp[-2] > 0 else 0
    
    # Price-to-rent ratio
    annual_rent = rp[-1] * 12
    median_price = hp[-1] * 1000
    p_to_r = median_price / annual_rent if annual_rent > 0 else 0
    
    # Affordability assessment
    monthly_mortgage = hp[-1] * 1000 * 0.0065  # rough 6.5% rate estimate
    if monthly_mortgage < rp[-1]:
        buy_assessment = "Buying is more affordable than renting"
    elif monthly_mortgage < rp[-1] * 1.2:
        buy_assessment = "Buying and renting are roughly comparable"
    else:
        buy_assessment = "Renting is more affordable than buying"
    
    home_chart = make_svg_chart(hp, [str(y) for y in years], '#2563eb', prefix='$', suffix='K')
    rent_chart = make_svg_chart(rp, [str(y) for y in years], '#10b981', prefix='$', suffix='')
    
    section = f'''
                    <div class="trend-section" style="background:#f8fafc;border-radius:12px;padding:24px;margin:20px 0;">
                        <h2>{name} Home Price Trends (2020-2026)</h2>
                        <div style="margin:16px 0;">
                            {home_chart}
                        </div>
                        <ul>
                            <li><strong>Median home price 2026:</strong> ${hp[-1]:,}K</li>
                            <li><strong>5-year change (2020-2026):</strong> {hp_5yr:+.1f}% (${hp[0]:,}K → ${hp[-1]:,}K)</li>
                            <li><strong>1-year change (2025-2026):</strong> {hp_1yr:+.1f}%</li>
                            <li><strong>Peak price:</strong> ${max(hp):,}K ({years[hp.index(max(hp))]})</li>
                        </ul>

                        <h2>{name} Rent Price Trends (2020-2026)</h2>
                        <div style="margin:16px 0;">
                            {rent_chart}
                        </div>
                        <ul>
                            <li><strong>Median rent 2026:</strong> ${rp[-1]:,}/month</li>
                            <li><strong>5-year change (2020-2026):</strong> {rp_5yr:+.1f}% (${rp[0]:,} → ${rp[-1]:,}/month)</li>
                            <li><strong>1-year change (2025-2026):</strong> {rp_1yr:+.1f}%</li>
                            <li><strong>Annual rent cost:</strong> ${annual_rent:,}/year</li>
                        </ul>

                        <h2>Buy vs Rent: {name} Price-to-Rent Ratio</h2>
                        <ul>
                            <li><strong>Price-to-rent ratio:</strong> {p_to_r:.1f} (median home price ÷ annual rent)</li>
                            <li><strong>Assessment:</strong> {buy_assessment}</li>
                            <li><strong>Rule of thumb:</strong> Ratio below 15 favors buying; above 20 favors renting; 15-20 is a toss-up</li>
                            <li><strong>Estimated monthly mortgage:</strong> ~${int(monthly_mortgage):,}/month (6.5% rate, 20% down)</li>
                            <li><strong>Monthly rent:</strong> ${rp[-1]:,}/month</li>
                        </ul>
                        <p><em>Data sources: Zillow Home Value Index, FRED, Census Bureau estimates. 2026 figures are projected based on recent trends.</em></p>
                    </div>
'''
    return section


# Process all 50 state pages
count = 0
for state_key in home_prices:
    fname = f'{state_key}-mortgage-calculator.html'
    fpath = os.path.join(site_dir, fname)
    if not os.path.exists(fpath):
        print(f'SKIP: {fname} not found')
        continue
    
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Check if trend section already exists
    if 'trend-section' in content:
        print(f'SKIP: {fname} already has trend section')
        continue
    
    trend_html = make_trend_section(state_key)
    if not trend_html:
        print(f'SKIP: {fname} - no data')
        continue
    
    # Insert before "Popular Cities" section, or before FAQ, or before the closing calc-content div
    # Try inserting after the "Average Home Price" section's closing </ul> before next <h2>
    # Best approach: insert before <h2>Popular Cities or before FAQ
    
    insert_markers = [
        '<h2>Popular Cities',
        '<h2>Frequently Asked Questions',
        '<div class="faq-section">',
        '<div class="related-calcs">'
    ]
    
    inserted = False
    for marker in insert_markers:
        idx = content.find(marker)
        if idx > 0:
            content = content[:idx] + trend_html + content[idx:]
            inserted = True
            break
    
    if not inserted:
        # Fallback: insert before </div> that closes calc-content
        idx = content.rfind('<div class="related-calcs">')
        if idx > 0:
            content = content[:idx] + trend_html + content[idx:]
            inserted = True
    
    if inserted:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        name = state_names.get(state_key, state_key)
        hp = home_prices[state_key]
        rp = rent_prices[state_key]
        print(f'OK: {fname} ({name}) - home ${hp[-1]}K, rent ${rp[-1]}')
    else:
        print(f'FAIL: {fname} - could not find insertion point')

print(f'\nTotal: {count}/50 state pages updated')

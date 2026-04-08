"""
批量生成美国各州房贷计算器页面
Programmatic SEO - 快速增加长尾流量
"""
import sys
import os
import re
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import config
except ImportError:
    print("Error: config.py not found")
    sys.exit(1)

# 各州房贷数据（2026年平均利率和首付比例）
STATE_DATA = {
    "California": {"rate": 6.5, "property_tax": 0.73, "insurance": 1500, "avg_price": 750000},
    "Texas": {"rate": 6.3, "property_tax": 1.80, "insurance": 2200, "avg_price": 350000},
    "Florida": {"rate": 6.4, "property_tax": 0.89, "insurance": 2800, "avg_price": 400000},
    "New-York": {"rate": 6.7, "property_tax": 1.69, "insurance": 1800, "avg_price": 550000},
    "Washington": {"rate": 6.2, "property_tax": 0.98, "insurance": 1200, "avg_price": 580000},
    "Arizona": {"rate": 6.3, "property_tax": 0.62, "insurance": 900, "avg_price": 420000},
    "Colorado": {"rate": 6.4, "property_tax": 0.51, "insurance": 1100, "avg_price": 520000},
    "Georgia": {"rate": 6.2, "property_tax": 0.92, "insurance": 1100, "avg_price": 340000},
    "North-Carolina": {"rate": 6.3, "property_tax": 0.78, "insurance": 950, "avg_price": 380000},
    "Nevada": {"rate": 6.4, "property_tax": 0.60, "insurance": 850, "avg_price": 410000},
    "Massachusetts": {"rate": 6.6, "property_tax": 1.23, "insurance": 1600, "avg_price": 580000},
    "Tennessee": {"rate": 6.2, "property_tax": 0.71, "insurance": 950, "avg_price": 330000},
    "Oregon": {"rate": 6.3, "property_tax": 0.87, "insurance": 1050, "avg_price": 470000},
    "Illinois": {"rate": 6.5, "property_tax": 1.98, "insurance": 1300, "avg_price": 280000},
    "Virginia": {"rate": 6.4, "property_tax": 0.82, "insurance": 950, "avg_price": 390000},
    "New-Jersey": {"rate": 6.8, "property_tax": 2.49, "insurance": 1700, "avg_price": 480000},
    "Ohio": {"rate": 6.2, "property_tax": 1.56, "insurance": 850, "avg_price": 240000},
    "Michigan": {"rate": 6.3, "property_tax": 1.37, "insurance": 950, "avg_price": 270000},
    "Pennsylvania": {"rate": 6.4, "property_tax": 1.58, "insurance": 1000, "avg_price": 250000},
    "Minnesota": {"rate": 6.3, "property_tax": 1.17, "insurance": 1100, "avg_price": 320000},
    "Wisconsin": {"rate": 6.2, "property_tax": 1.85, "insurance": 900, "avg_price": 260000},
    "Maryland": {"rate": 6.5, "property_tax": 1.09, "insurance": 1300, "avg_price": 380000},
    "South-Carolina": {"rate": 6.2, "property_tax": 0.55, "insurance": 1100, "avg_price": 320000},
    "Alabama": {"rate": 6.1, "property_tax": 0.41, "insurance": 900, "avg_price": 240000},
    "Louisiana": {"rate": 6.2, "property_tax": 0.55, "insurance": 1200, "avg_price": 230000},
    "Kentucky": {"rate": 6.2, "property_tax": 0.86, "insurance": 850, "avg_price": 230000},
    "Oklahoma": {"rate": 6.1, "property_tax": 0.82, "insurance": 1300, "avg_price": 200000},
    "Connecticut": {"rate": 6.6, "property_tax": 2.14, "insurance": 1800, "avg_price": 380000},
    "Iowa": {"rate": 6.0, "property_tax": 1.52, "insurance": 750, "avg_price": 210000},
    "Kansas": {"rate": 6.1, "property_tax": 1.41, "insurance": 1100, "avg_price": 230000},
    "Arkansas": {"rate": 6.1, "property_tax": 0.62, "insurance": 900, "avg_price": 200000},
    "Mississippi": {"rate": 6.1, "property_tax": 0.63, "insurance": 950, "avg_price": 190000},
    "Nebraska": {"rate": 6.0, "property_tax": 1.76, "insurance": 900, "avg_price": 240000},
    "Idaho": {"rate": 6.2, "property_tax": 0.67, "insurance": 750, "avg_price": 400000},
    "New-Mexico": {"rate": 6.2, "property_tax": 0.77, "insurance": 850, "avg_price": 280000},
    "Utah": {"rate": 6.3, "property_tax": 0.58, "insurance": 850, "avg_price": 480000},
    "Indiana": {"rate": 6.2, "property_tax": 0.84, "insurance": 850, "avg_price": 260000},
    "Missouri": {"rate": 6.2, "property_tax": 0.97, "insurance": 950, "avg_price": 230000},
    "Montana": {"rate": 6.3, "property_tax": 0.83, "insurance": 1050, "avg_price": 420000},
    "Alaska": {"rate": 6.4, "property_tax": 1.09, "insurance": 1300, "avg_price": 320000},
    "North-Dakota": {"rate": 6.0, "property_tax": 1.42, "insurance": 900, "avg_price": 240000},
    "South-Dakota": {"rate": 6.0, "property_tax": 1.32, "insurance": 850, "avg_price": 280000},
    "West-Virginia": {"rate": 6.2, "property_tax": 0.58, "insurance": 850, "avg_price": 140000},
    "Delaware": {"rate": 6.4, "property_tax": 0.57, "insurance": 850, "avg_price": 320000},
    "Rhode-Island": {"rate": 6.6, "property_tax": 1.63, "insurance": 1600, "avg_price": 380000},
    "Vermont": {"rate": 6.4, "property_tax": 1.86, "insurance": 1100, "avg_price": 280000},
    "New-Hampshire": {"rate": 6.5, "property_tax": 2.05, "insurance": 1300, "avg_price": 420000},
    "Maine": {"rate": 6.3, "property_tax": 1.09, "insurance": 950, "avg_price": 300000},
    "Hawaii": {"rate": 6.8, "property_tax": 0.28, "insurance": 900, "avg_price": 830000},
    "Wyoming": {"rate": 6.1, "property_tax": 0.61, "insurance": 900, "avg_price": 320000},
}

def generate_state_page(state, data):
    """生成单个州的房贷计算器页面"""
    state_display = state.replace("-", " ")
    state_kebab = state.lower()
    avg_price = data.get("avg_price", 300000)
    default_down = int(avg_price * 0.2)
    default_rate = data.get("rate", 6.5)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{state_display} Mortgage Calculator - Free {state_display} Home Loan Calculator | CalcWithMe</title>
    <meta name="description" content="Free {state_display} mortgage calculator. Calculate monthly payments, compare rates, and estimate {state_display} home loan costs. Updated 2026 rates for {state_display} homebuyers.">
    <meta name="keywords" content="{state_display} mortgage calculator, {state_display} home loan, {state_display} mortgage rates, {state_display} loan calculator">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://calcwithme.com/{state_kebab}-mortgage-calculator.html">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>%E2%83%A3</text></svg>">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "{state_display} Mortgage Calculator",
        "url": "https://calcwithme.com/{state_kebab}-mortgage-calculator.html",
        "description": "Free {state_display} mortgage calculator with current 2026 rates",
        "applicationCategory": "FinanceApplication",
        "offers": {{"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    }}
    </script>
</head>
<body>
    <header>
        <div class="container header-inner">
            <a href="/" class="logo"><span class="logo-icon">&#x1F522;</span><span>Calc<span class="highlight">With</span>Me</span></a>
            <nav><a href="/#calculators">Calculators</a><a href="/#about">About</a><a href="../mortgage-calculator.html">General Mortgage</a></nav>
        </div>
    </header>
    <main class="calculator-page">
        <div class="container">
            <div class="calculator-layout">
                <div class="calculator-main">
                    <h1>{state_display} Mortgage Calculator</h1>
                    <p class="page-desc">Calculate your monthly mortgage payment in {state_display}. Updated with current 2026 {state_display} mortgage rates, property taxes, and home insurance estimates. The #1 free {state_display} mortgage calculator.</p>
                    <div class="calc-form">
                        <div class="form-group"><label for="homePrice">Home Price</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="homePrice" class="has-prefix" value="{avg_price}" min="1000" step="1000"></div></div>
                        <div class="form-row">
                            <div class="form-group"><label for="downPayment">Down Payment</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="downPayment" class="has-prefix" value="{default_down}" min="0" step="1000"></div></div>
                            <div class="form-group"><label for="downPaymentPct">Down %</label><div class="input-wrapper"><input type="number" id="downPaymentPct" value="20" step="0.5"><span class="input-suffix">%</span></div></div>
                        </div>
                        <div class="form-row">
                            <div class="form-group"><label for="loanTerm">Loan Term</label><select id="loanTerm"><option value="30" selected>30 Years</option><option value="15">15 Years</option></select></div>
                            <div class="form-group"><label for="interestRate">Interest Rate</label><div class="input-wrapper"><input type="number" id="interestRate" value="{default_rate}" step="0.05"><span class="input-suffix">%</span></div></div>
                        </div>
                        <div class="form-group"><label for="stateTax">Property Tax Rate (Annual %)</label><div class="input-wrapper"><input type="number" id="stateTax" value="{data.get("property_tax", 1.0)}" step="0.01"><span class="input-suffix">%</span></div></div>
                        <button class="btn-calculate" onclick="calculateMortgage()">Calculate Payment</button>
                    </div>
                    <div class="ad-container">Advertisement Space - Google AdSense</div>
                    <div class="calc-content">
                        <h2>Understanding Mortgage Rates in {state_display}</h2>
                        <p>{state_display} mortgage rates vary based on your credit score, loan type, and down payment. As of 2026, average {state_display} mortgage rates are around {default_rate}% for a 30-year fixed loan. Use our calculator above to see how different rates and home prices affect your monthly payment.</p>
                        <h3>How Property Taxes Work in {state_display}</h3>
                        <p>{state_display} has an average property tax rate of {data.get("property_tax", 1.0)}%. Property taxes are typically included in your monthly mortgage payment as part of PITI (Principal, Interest, Taxes, and Insurance).</p>
                        <h3>How to Get the Best Mortgage Rate in {state_display}</h3>
                        <ul>
                            <li><strong>Improve your credit score</strong> - A score of 740+ typically gets the best rates</li>
                            <li><strong>Save for a larger down payment</strong> - 20%+ down can lower your rate and eliminate PMI</li>
                            <li><strong>Compare multiple lenders</strong> - Rates vary between lenders by 0.25-0.5%</li>
                            <li><strong>Consider different loan types</strong> - FHA, VA, and USDA loans offer lower rates for qualifying buyers</li>
                        </ul>
                        <h3>{state_display} First-Time Homebuyer Programs</h3>
                        <p>{state_display} offers several first-time homebuyer programs including down payment assistance, reduced interest rates, and tax credits. Check with your local housing authority for specific programs available in {state_display}.</p>
                        <div class="related-calcs">
                            <h3>Related Calculators</h3>
                            <a href="../mortgage-calculator.html">General Mortgage Calculator</a>
                            <a href="../loan-calculator.html">Loan Calculator</a>
                            <a href="../compound-interest-calculator.html">Compound Interest Calculator</a>
                            <a href="../rent-vs-buy-calculator.html">Rent vs Buy Calculator</a>
                        </div>
                    </div>
                </div>
                <aside class="results-panel">
                    <h2>&#x1F4CA; Your Results</h2>
                    <div class="result-item"><p class="result-label">Monthly Payment (PITI)</p><p class="result-value" id="monthlyPayment">$0</p></div>
                    <div class="result-item"><p class="result-label">Principal & Interest</p><p class="result-value secondary" id="monthlyPI">$0</p></div>
                    <div class="result-item"><p class="result-label">Property Tax</p><p class="result-value secondary" id="monthlyTax">$0</p></div>
                    <div class="result-item"><p class="result-label">Total Interest</p><p class="result-value secondary" id="totalInterest" style="color:#dc2626;">$0</p></div>
                    <div class="result-item"><p class="result-label">Loan Amount</p><p class="result-value secondary" id="loanAmount">$0</p></div>
                </aside>
            </div>
        </div>
    </main>
    <footer>
        <div class="container">
            <div class="footer-inner">
                <div class="footer-brand"><span class="logo-icon">&#x1F522;</span><span>CalcWithMe</span><p>Free financial calculators.</p></div>
                <div class="footer-links"><h4>Popular</h4><a href="../mortgage-calculator.html">Mortgage Calculator</a><a href="../loan-calculator.html">Loan Calculator</a><a href="../compound-interest-calculator.html">Compound Interest</a></div>
                <div class="footer-links"><h4>More</h4><a href="../auto-loan-calculator.html">Auto Loan</a><a href="../retirement-calculator.html">Retirement</a><a href="../salary-calculator.html">Salary</a></div>
            </div>
            <div class="footer-bottom"><p>&#169; 2026 CalcWithMe.com.</p></div>
        </div>
    </footer>
    <script>
    document.getElementById('homePrice').addEventListener('input', syncDownPayment);
    document.getElementById('downPayment').addEventListener('input', syncDownPaymentPct);
    document.getElementById('downPaymentPct').addEventListener('input', syncDownPaymentFromPct);
    
    function syncDownPayment() {{
        const hp = parseFloat(document.getElementById('homePrice').value)||0;
        const dp = parseFloat(document.getElementById('downPayment').value)||0;
        document.getElementById('downPaymentPct').value = hp>0 ? (dp/hp*100).toFixed(1) : 0;
    }}
    function syncDownPaymentPct() {{
        const hp = parseFloat(document.getElementById('homePrice').value)||0;
        const dp = parseFloat(document.getElementById('downPayment').value)||0;
        document.getElementById('downPaymentPct').value = hp>0 ? (dp/hp*100).toFixed(1) : 0;
    }}
    function syncDownPaymentFromPct() {{
        const hp = parseFloat(document.getElementById('homePrice').value)||0;
        const pct = parseFloat(document.getElementById('downPaymentPct').value)||0;
        document.getElementById('downPayment').value = Math.round(hp*pct/100);
    }}
    
    function calculateMortgage() {{
        const hp = parseFloat(document.getElementById('homePrice').value)||0;
        const dp = parseFloat(document.getElementById('downPayment').value)||0;
        const years = parseInt(document.getElementById('loanTerm').value)||30;
        const rate = parseFloat(document.getElementById('interestRate').value)||0;
        const stateTax = parseFloat(document.getElementById('stateTax').value)||0;
        
        const loan = hp - dp;
        const mr = rate/100/12;
        const n = years * 12;
        const pi = mr===0 ? loan/n : loan*(mr*Math.pow(1+mr,n))/(Math.pow(1+mr,n)-1);
        const monthlyTax = hp * stateTax/100/12;
        const total = pi + monthlyTax;
        const totalInt = pi*n - loan;
        
        document.getElementById('monthlyPayment').textContent = '$'+fmt(Math.round(total));
        document.getElementById('monthlyPI').textContent = '$'+fmt(Math.round(pi));
        document.getElementById('monthlyTax').textContent = '$'+fmt(Math.round(monthlyTax));
        document.getElementById('totalInterest').textContent = '$'+fmt(Math.round(totalInt));
        document.getElementById('loanAmount').textContent = '$'+fmt(loan);
    }}
    function fmt(n){{return n.toString().replace(/\\B(?=(\\d{{3}})+(?!\d))/g,',');}}
    window.addEventListener('load', calculateMortgage);
    </script>
</body>
</html>'''
    return html

def update_sitemap_with_states(states):
    """更新sitemap包含所有州页面"""
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # 主页面
    sitemap += '  <url><loc>https://calcwithme.com/</loc><lastmod>2026-04-06</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>\n'
    
    # 通用计算器
    pages = [
        "mortgage-calculator", "loan-calculator", "compound-interest-calculator",
        "auto-loan-calculator", "credit-card-payoff-calculator", "retirement-calculator",
        "salary-calculator", "investment-roi-calculator", "rent-vs-buy-calculator",
        "savings-goal-calculator"
    ]
    for page in pages:
        sitemap += f'  <url><loc>https://calcwithme.com/{page}.html</loc><lastmod>2026-04-06</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n'
    
    # 各州页面
    for state in states:
        state_kebab = state.lower()
        sitemap += f'  <url><loc>https://calcwithme.com/{state_kebab}-mortgage-calculator.html</loc><lastmod>2026-04-06</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n'
    
    sitemap += '</urlset>\n'
    return sitemap

def update_sitemap_temp(states):
    """临时sitemap用Netlify地址"""
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += '  <url><loc>https://subtle-kelpie-9a9a41.netlify.app/</loc><lastmod>2026-04-06</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>\n'
    pages = [
        "mortgage-calculator", "loan-calculator", "compound-interest-calculator",
        "auto-loan-calculator", "credit-card-payoff-calculator", "retirement-calculator",
        "salary-calculator", "investment-roi-calculator", "rent-vs-buy-calculator",
        "savings-goal-calculator"
    ]
    for page in pages:
        sitemap += f'  <url><loc>https://subtle-kelpie-9a9a41.netlify.app/{page}.html</loc><lastmod>2026-04-06</lastlastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n'
    for state in states:
        state_kebab = state.lower()
        sitemap += f'  <url><loc>https://subtle-kelpie-9a9a41.netlify.app/{state_kebab}-mortgage-calculator.html</loc><lastmod>2026-04-06</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n'
    sitemap += '</urlset>\n'
    return sitemap

def main():
    print("\n" + "="*60)
    print("Generating State Mortgage Calculator Pages")
    print("="*60)
    
    output_dir = os.path.join(config.LOCAL_SITE_PATH, "state-pages")
    os.makedirs(output_dir, exist_ok=True)
    
    generated = 0
    for state, data in STATE_DATA.items():
        state_kebab = state.lower()
        filename = f"{state_kebab}-mortgage-calculator.html"
        filepath = os.path.join(output_dir, filename)
        
        content = generate_state_page(state, data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ Generated: {filename}")
        generated += 1
    
    print(f"\nGenerated {generated} state pages")
    
    # 生成新sitemap
    sitemap_content = update_sitemap_temp(list(STATE_DATA.keys()))
    sitemap_path = os.path.join(config.LOCAL_SITE_PATH, "sitemap-new.xml")
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print(f"\n  ✅ New sitemap saved: sitemap-new.xml")
    print(f"     Total URLs: {len(STATE_DATA) + 11}")
    
    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("  1. Copy all files from state-pages/ to calcwithme-site/")
    print("  2. Replace sitemap.xml with sitemap-new.xml")
    print("  3. Upload to Netlify")
    print("  4. Submit sitemap-new.xml to Google Search Console")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()

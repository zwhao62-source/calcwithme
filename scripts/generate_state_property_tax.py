#!/usr/bin/env python3
"""Generate 50 state property tax pages for CalcWithMe."""
import os

STATES = {
    "Alabama": {"abbrev": "al", "rate": 0.0041, "avg_tax": 820, "median_home": 170600, "assessment": "100%"},
    "Alaska": {"abbrev": "ak", "rate": 0.0114, "avg_tax": 3780, "median_home": 331600, "assessment": "100%"},
    "Arizona": {"abbrev": "az", "rate": 0.0051, "avg_tax": 1800, "median_home": 353500, "assessment": "100% (limited rate increases)"},
    "Arkansas": {"abbrev": "ar", "rate": 0.0062, "avg_tax": 1200, "median_home": 193700, "assessment": "20%"},
    "California": {"abbrev": "ca", "rate": 0.0077, "avg_tax": 4860, "median_home": 631200, "assessment": "100% (Prop 13 caps at 2%/yr)"},
    "Colorado": {"abbrev": "co", "rate": 0.0051, "avg_tax": 2500, "median_home": 490200, "assessment": "7.15% residential"},
    "Connecticut": {"abbrev": "ct", "rate": 0.0215, "avg_tax": 6680, "median_home": 310800, "assessment": "70%"},
    "Delaware": {"abbrev": "de", "rate": 0.0056, "avg_tax": 1760, "median_home": 314600, "assessment": "100%"},
    "Florida": {"abbrev": "fl", "rate": 0.0097, "avg_tax": 2980, "median_home": 307400, "assessment": "100% (Save Our Homes cap 3%/yr)"},
    "Georgia": {"abbrev": "ga", "rate": 0.0092, "avg_tax": 2560, "median_home": 278400, "assessment": "40%"},
    "Hawaii": {"abbrev": "hi", "rate": 0.0029, "avg_tax": 2190, "median_home": 755800, "assessment": "100%"},
    "Idaho": {"abbrev": "id", "rate": 0.0069, "avg_tax": 1980, "median_home": 287100, "assessment": "100%"},
    "Illinois": {"abbrev": "il", "rate": 0.0222, "avg_tax": 5370, "median_home": 241800, "assessment": "33.33%"},
    "Indiana": {"abbrev": "in", "rate": 0.0085, "avg_tax": 1650, "median_home": 194300, "assessment": "100%"},
    "Iowa": {"abbrev": "ia", "rate": 0.0154, "avg_tax": 3010, "median_home": 195500, "assessment": "100%"},
    "Kansas": {"abbrev": "ks", "rate": 0.0141, "avg_tax": 2780, "median_home": 197100, "assessment": "11.5-25%"},
    "Kentucky": {"abbrev": "ky", "rate": 0.0074, "avg_tax": 1390, "median_home": 188200, "assessment": "100%"},
    "Louisiana": {"abbrev": "la", "rate": 0.0055, "avg_tax": 1150, "median_home": 209300, "assessment": "10%"},
    "Maine": {"abbrev": "me", "rate": 0.0113, "avg_tax": 3130, "median_home": 277200, "assessment": "100%"},
    "Maryland": {"abbrev": "md", "rate": 0.0109, "avg_tax": 3920, "median_home": 359600, "assessment": "100%"},
    "Massachusetts": {"abbrev": "ma", "rate": 0.0115, "avg_tax": 5270, "median_home": 458800, "assessment": "100%"},
    "Michigan": {"abbrev": "mi", "rate": 0.0159, "avg_tax": 2960, "median_home": 186400, "assessment": "50%"},
    "Minnesota": {"abbrev": "mn", "rate": 0.0105, "avg_tax": 3140, "median_home": 299400, "assessment": "100%"},
    "Mississippi": {"abbrev": "ms", "rate": 0.0081, "avg_tax": 1270, "median_home": 156800, "assessment": "10%"},
    "Missouri": {"abbrev": "mo", "rate": 0.0099, "avg_tax": 1800, "median_home": 181800, "assessment": "19%"},
    "Montana": {"abbrev": "mt", "rate": 0.0084, "avg_tax": 2480, "median_home": 295200, "assessment": "100%"},
    "Nebraska": {"abbrev": "ne", "rate": 0.0176, "avg_tax": 3470, "median_home": 197200, "assessment": "75-95%"},
    "Nevada": {"abbrev": "nv", "rate": 0.0055, "avg_tax": 2180, "median_home": 396300, "assessment": "35%"},
    "New Hampshire": {"abbrev": "nh", "rate": 0.0203, "avg_tax": 6760, "median_home": 333200, "assessment": "100%"},
    "New Jersey": {"abbrev": "nj", "rate": 0.0249, "avg_tax": 9640, "median_home": 387200, "assessment": "100%"},
    "New Mexico": {"abbrev": "nm", "rate": 0.0071, "avg_tax": 1720, "median_home": 242600, "assessment": "100% (3% cap)"},
    "New York": {"abbrev": "ny", "rate": 0.0172, "avg_tax": 6170, "median_home": 358700, "assessment": "Varies by municipality"},
    "North Carolina": {"abbrev": "nc", "rate": 0.0084, "avg_tax": 1860, "median_home": 221300, "assessment": "100%"},
    "North Dakota": {"abbrev": "nd", "rate": 0.0102, "avg_tax": 2430, "median_home": 238300, "assessment": "50%"},
    "Ohio": {"abbrev": "oh", "rate": 0.0136, "avg_tax": 2560, "median_home": 188300, "assessment": "35%"},
    "Oklahoma": {"abbrev": "ok", "rate": 0.0090, "avg_tax": 1470, "median_home": 163200, "assessment": "11-13.5%"},
    "Oregon": {"abbrev": "or", "rate": 0.0093, "avg_tax": 3460, "median_home": 371800, "assessment": "100% (3% cap)"},
    "Pennsylvania": {"abbrev": "pa", "rate": 0.0150, "avg_tax": 3370, "median_home": 224600, "assessment": "100%"},
    "Rhode Island": {"abbrev": "ri", "rate": 0.0163, "avg_tax": 4910, "median_home": 301300, "assessment": "100%"},
    "South Carolina": {"abbrev": "sc", "rate": 0.0057, "avg_tax": 1210, "median_home": 212700, "assessment": "6% (owner-occupied)"},
    "South Dakota": {"abbrev": "sd", "rate": 0.0129, "avg_tax": 2640, "median_home": 204500, "assessment": "85%"},
    "Tennessee": {"abbrev": "tn", "rate": 0.0068, "avg_tax": 1590, "median_home": 234000, "assessment": "25%"},
    "Texas": {"abbrev": "tx", "rate": 0.0181, "avg_tax": 4560, "median_home": 252100, "assessment": "100% (10% homestead cap)"},
    "Utah": {"abbrev": "ut", "rate": 0.0063, "avg_tax": 2600, "median_home": 412800, "assessment": "100%"},
    "Vermont": {"abbrev": "vt", "rate": 0.0192, "avg_tax": 4940, "median_home": 257300, "assessment": "100%"},
    "Virginia": {"abbrev": "va", "rate": 0.0082, "avg_tax": 2480, "median_home": 302400, "assessment": "100%"},
    "Washington": {"abbrev": "wa", "rate": 0.0098, "avg_tax": 4180, "median_home": 426400, "assessment": "100% (1% cap)"},
    "West Virginia": {"abbrev": "wv", "rate": 0.0058, "avg_tax": 990, "median_home": 170700, "assessment": "60%"},
    "Wisconsin": {"abbrev": "wi", "rate": 0.0185, "avg_tax": 4070, "median_home": 220100, "assessment": "100%"},
    "Wyoming": {"abbrev": "wy", "rate": 0.0058, "avg_tax": 1540, "median_home": 265300, "assessment": "9.5%"}
}

def generate_page(state, data):
    ab = data["abbrev"]
    rate = data["rate"]
    avg_tax = data["avg_tax"]
    median = data["median_home"]
    assessment = data["assessment"]
    rate_pct = f"{rate*100:.2f}"
    
    # Neighboring states for comparison
    neighbors = get_neighbors(ab)
    neighbor_rows = ""
    for n_state, n_ab in neighbors:
        if n_state in STATES:
            nd = STATES[n_state]
            neighbor_rows += f'<div class="breakdown-row"><span>{n_state}</span><span>{nd["rate"]*100:.2f}%</span></div>\n                        '
    
    monthly_tax = round(avg_tax / 12)
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{state} Property Tax Calculator 2026 - {rate_pct}% Effective Rate | CalcWithMe</title>
    <meta name="description" content="{state} property tax calculator 2026. Effective rate {rate_pct}%, average annual tax ${avg_tax:,}, median home value ${median:,}. Calculate your {state} property taxes.">
    <meta name="keywords" content="{state} property tax calculator, {state} property tax rate, {ab} property tax, {state} real estate tax">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://calcwithme.com/{ab}-property-tax.html">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏛️</text></svg>">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://calcwithme.com/"}},
      {{"@type":"ListItem","position":2,"name":"Property Tax by State","item":"https://calcwithme.com/property-tax-calculator.html"}},
      {{"@type":"ListItem","position":3,"name":"{state}","item":"https://calcwithme.com/{ab}-property-tax.html"}}
    ]}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {{"@type":"Question","name":"What is the property tax rate in {state}?","acceptedAnswer":{{"@type":"Answer","text":"The effective property tax rate in {state} is {rate_pct}% as of 2026. On a home valued at ${{median:,}}, the annual property tax is approximately ${{avg_tax:,}}."}}}},
      {{"@type":"Question","name":"How are properties assessed in {state}?","acceptedAnswer":{{"@type":"Answer","text":"In {state}, properties are assessed at {assessment} of market value. The assessment ratio determines the taxable value used to calculate your property tax bill."}}}}
    ]}}
    </script>
    <script defer src="https://cloud.umami.is/script.js" data-website-id="77de646f-0376-43ee-8b45-326250fd1485"></script>
</head>
<body>
    <header><div class="container header-inner"><a href="/" class="logo"><span class="logo-icon">&#x1F522;</span><span>Calc<span class="highlight">With</span>Me</span></a><nav><a href="/#calculators">Calculators</a><a href="/#about">About</a><a href="/blog">Blog</a><a href="/savings-tips.html">&#x1F4B0; Money Tips</a><a href="/mortgage-calculator.html">Mortgage</a></nav></div></header>

    <main class="calculator-page">
        <div class="container">
            <div class="calculator-layout">
                <div class="calculator-main">
                    <h1>{state} Property Tax Calculator 2026</h1>
                    <p class="page-desc">Calculate your {state} property taxes — <strong>effective rate {rate_pct}%, average annual tax ${avg_tax:,}</strong>. Updated June 2026.</p>
                    <div class="calc-form">
                        <div class="form-group"><label for="ptVal">Your Home Value in {state}</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="ptVal" class="has-prefix" value="{median}" min="0"></div></div>
                        <button class="btn-calculate" onclick="calcPT()">Calculate {state} Property Tax</button>
                    </div>
                    <div class="ad-container">Advertisement Space — Google AdSense</div>
                    <div class="calc-content">
                        <h2>{state} Property Tax Overview</h2>
                        <p>{state} has an <strong>effective property tax rate of {rate_pct}%</strong>, making it {rank_text(rate)} among all 50 states. The average annual property tax in {state} is <strong>${avg_tax:,}</strong> on a median home value of ${median:,}.</p>
                        <ul>
                            <li><strong>Effective tax rate:</strong> {rate_pct}%</li>
                            <li><strong>Assessment ratio:</strong> {assessment}</li>
                            <li><strong>Median home value:</strong> ${median:,}</li>
                            <li><strong>Average annual tax:</strong> ${avg_tax:,} (${monthly_tax}/month)</li>
                        </ul>

                        <h2>How {state} Property Tax Works</h2>
                        <p>{state} properties are assessed at <strong>{assessment}</strong> of market value. The assessed value is then multiplied by the local millage rate to determine your annual tax bill.</p>
                        <p style="background:#f1f5f9;padding:12px 16px;border-radius:8px;"><strong>{state} Property Tax = Assessed Value × Local Millage Rate</strong></p>
                        <p>Local millage rates vary by county, city, school district, and special districts within {state}. Your total rate is the sum of all applicable levies.</p>

                        <h2>{state} Property Tax Exemptions</h2>
                        <ul>
                            <li><strong>Homestead exemption:</strong> {homestead(state)}</li>
                            <li><strong>Senior exemption:</strong> {senior(state)}</li>
                            <li><strong>Veteran exemption:</strong> {veteran(state)}</li>
                            <li><strong>Disability exemption:</strong> {disability(state)}</li>
                        </ul>

                        <h2>How {state} Compares to Neighboring States</h2>
                        <div class="results-breakdown" style="margin-top:8px;">
                            <div class="breakdown-row"><strong><span>State</span></strong><strong><span>Effective Rate</span></strong></div>
                            <div class="breakdown-row" style="background:#eff6ff;"><span>{state}</span><span style="font-weight:700;">{rate_pct}%</span></div>
                            {neighbor_rows}
                            <div class="breakdown-row"><span>National Average</span><span>1.08%</span></div>
                        </div>

                        <h2>How to Appeal Your {state} Property Tax</h2>
                        <p>If you believe your {state} property is over-assessed, you have the right to appeal:</p>
                        <ul>
                            <li><strong>1. Contact your county assessor</strong> — Review your assessment for errors in square footage, lot size, or condition</li>
                            <li><strong>2. Gather comparable sales</strong> — Find 3-5 similar homes sold recently in your {state} neighborhood with lower values</li>
                            <li><strong>3. File by the deadline</strong> — {state} appeal deadlines vary by county; check your assessment notice</li>
                            <li><strong>4. Present evidence</strong> — Focus on facts and comparable data, not complaints about tax rates</li>
                            <li><strong>5. Success rate:</strong> 50-70% of {state} property tax appeals result in a reduction</li>
                        </ul>

                        <div class="related-calcs"><h3>Related Calculators</h3><a href="property-tax-calculator.html">Property Tax Calculator</a><a href="mortgage-calculator.html">Mortgage Calculator</a><a href="closing-cost-calculator.html">Closing Costs</a><a href="home-affordability-calculator.html">Home Affordability</a></div>
                    </div>

                    <div class="faq-section">
                        <h3>Frequently Asked Questions</h3>
                        <details class="faq-item"><summary>What is the property tax rate in {state}?</summary><p>The effective property tax rate in {state} is {rate_pct}% as of 2026. On a home valued at ${median:,}, the annual property tax is approximately ${avg_tax:,}.</p></details>
                        <details class="faq-item"><summary>How are properties assessed in {state}?</summary><p>In {state}, properties are assessed at {assessment} of market value. The assessed value determines the taxable value used to calculate your property tax bill.</p></details>
                    </div>
                </div>

                <aside class="results-panel">
                    <h2>&#x1F4CA; {state} Property Tax</h2>
                    <div class="result-item"><p class="result-label">Annual Property Tax</p><p class="result-value" id="ptAnnual" style="color:#2563eb;">$0</p></div>
                    <div class="result-item"><p class="result-label">Monthly Property Tax</p><p class="result-value" id="ptMonthly" style="color:#10b981;">$0</p></div>
                    <div class="result-item"><p class="result-label">Effective Rate</p><p class="result-value" id="ptRateShow">{rate_pct}%</p></div>
                    <div class="results-breakdown">
                        <h3 style="font-size:0.95rem;font-weight:700;margin-bottom:12px;">5-Year Projection (3%/yr increase)</h3>
                        <div class="breakdown-row"><span>Year 1</span><span id="ptY1">$0</span></div>
                        <div class="breakdown-row"><span>Year 2</span><span id="ptY2">$0</span></div>
                        <div class="breakdown-row"><span>Year 3</span><span id="ptY3">$0</span></div>
                        <div class="breakdown-row"><span>Year 4</span><span id="ptY4">$0</span></div>
                        <div class="breakdown-row"><span>Year 5</span><span id="ptY5">$0</span></div>
                        <div class="breakdown-row" style="border-top:2px solid #e2e8f0;padding-top:8px;margin-top:8px;"><strong><span>5-Year Total</span></strong><strong><span id="pt5yr">$0</span></strong></div>
                    </div>
                </aside>
            </div>
        </div>
    </main>

    <footer><div class="container"><div class="footer-inner"><div class="footer-brand"><span class="logo-icon">&#x1F522;</span><span>CalcWithMe</span><p>Free financial calculators.</p></div><div class="footer-links"><h4>Popular</h4><a href="mortgage-calculator.html">Mortgage</a><a href="loan-calculator.html">Loan</a><a href="compound-interest-calculator.html">Compound Interest</a></div><div class="footer-links"><h4>More</h4><a href="auto-loan-calculator.html">Auto Loan</a><a href="retirement-calculator.html">Retirement</a><a href="salary-calculator.html">Salary</a></div></div><div class="footer-bottom"><p>&#169; 2026 CalcWithMe.com.</p></div></div></footer>

    <script>
    function calcPT() {{
        const val = parseFloat(document.getElementById('ptVal').value) || 0;
        const rate = {rate};
        const fmt = v => '$' + Math.round(v).toLocaleString();
        const annual = val * rate;
        const monthly = annual / 12;
        const y1=annual, y2=y1*1.03, y3=y2*1.03, y4=y3*1.03, y5=y4*1.03;
        document.getElementById('ptAnnual').textContent = fmt(annual);
        document.getElementById('ptMonthly').textContent = fmt(monthly);
        document.getElementById('ptY1').textContent = fmt(y1);
        document.getElementById('ptY2').textContent = fmt(y2);
        document.getElementById('ptY3').textContent = fmt(y3);
        document.getElementById('ptY4').textContent = fmt(y4);
        document.getElementById('ptY5').textContent = fmt(y5);
        document.getElementById('pt5yr').textContent = fmt(y1+y2+y3+y4+y5);
    }}
    window.addEventListener('load', calcPT);
    </script>
    <div class="visitor-counter"><span>👁️ Visitors: </span><span id="visitor-counter" style="display:none;">0</span></div>
    <script src="js/visitor-counter.js"></script>
</body>
</html>'''


def get_neighbors(abbrev):
    neighbor_map = {
        "al": [("Tennessee", "tn"), ("Georgia", "ga"), ("Mississippi", "ms"), ("Florida", "fl")],
        "ak": [],
        "az": [("California", "ca"), ("Nevada", "nv"), ("New Mexico", "nm"), ("Utah", "ut")],
        "ar": [("Missouri", "mo"), ("Tennessee", "tn"), ("Mississippi", "ms"), ("Louisiana", "la"), ("Texas", "tx"), ("Oklahoma", "ok")],
        "ca": [("Oregon", "or"), ("Nevada", "nv"), ("Arizona", "az")],
        "co": [("Wyoming", "wy"), ("Nebraska", "ne"), ("Kansas", "ks"), ("Oklahoma", "ok"), ("New Mexico", "nm"), ("Arizona", "az"), ("Utah", "ut")],
        "ct": [("New York", "ny"), ("Massachusetts", "ma"), ("Rhode Island", "ri")],
        "de": [("Maryland", "md"), ("Pennsylvania", "pa"), ("New Jersey", "nj")],
        "fl": [("Georgia", "ga"), ("Alabama", "al")],
        "ga": [("Tennessee", "tn"), ("North Carolina", "nc"), ("South Carolina", "sc"), ("Florida", "fl"), ("Alabama", "al")],
        "hi": [],
        "id": [("Montana", "mt"), ("Wyoming", "wy"), ("Nevada", "nv"), ("Utah", "ut"), ("Washington", "wa"), ("Oregon", "or")],
        "il": [("Wisconsin", "wi"), ("Indiana", "in"), ("Kentucky", "ky"), ("Missouri", "mo"), ("Iowa", "ia")],
        "in": [("Michigan", "mi"), ("Ohio", "oh"), ("Kentucky", "ky"), ("Illinois", "il")],
        "ia": [("Minnesota", "mn"), ("Wisconsin", "wi"), ("Illinois", "il"), ("Missouri", "mo"), ("South Dakota", "sd"), ("Nebraska", "ne")],
        "ks": [("Nebraska", "ne"), ("Missouri", "mo"), ("Oklahoma", "ok"), ("Colorado", "co")],
        "ky": [("Illinois", "il"), ("Indiana", "in"), ("Ohio", "oh"), ("West Virginia", "wv"), ("Virginia", "va"), ("Tennessee", "tn"), ("Missouri", "mo")],
        "la": [("Arkansas", "ar"), ("Mississippi", "ms"), ("Texas", "tx")],
        "me": [("New Hampshire", "nh")],
        "md": [("Pennsylvania", "pa"), ("Delaware", "de"), ("Virginia", "va"), ("West Virginia", "wv")],
        "ma": [("New Hampshire", "nh"), ("Vermont", "vt"), ("Connecticut", "ct"), ("Rhode Island", "ri")],
        "mi": [("Wisconsin", "wi"), ("Indiana", "in"), ("Ohio", "oh")],
        "mn": [("North Dakota", "nd"), ("South Dakota", "sd"), ("Iowa", "ia"), ("Wisconsin", "wi")],
        "ms": [("Tennessee", "tn"), ("Alabama", "al"), ("Louisiana", "la"), ("Arkansas", "ar")],
        "mo": [("Iowa", "ia"), ("Illinois", "il"), ("Kentucky", "ky"), ("Tennessee", "tn"), ("Arkansas", "ar"), ("Oklahoma", "ok"), ("Kansas", "ks"), ("Nebraska", "ne")],
        "mt": [("North Dakota", "nd"), ("South Dakota", "sd"), ("Wyoming", "wy"), ("Idaho", "id")],
        "ne": [("South Dakota", "sd"), ("Iowa", "ia"), ("Missouri", "mo"), ("Kansas", "ks"), ("Colorado", "co"), ("Wyoming", "wy")],
        "nv": [("Oregon", "or"), ("Idaho", "id"), ("Utah", "ut"), ("Arizona", "az"), ("California", "ca")],
        "nh": [("Maine", "me"), ("Vermont", "vt"), ("Massachusetts", "ma")],
        "nj": [("New York", "ny"), ("Pennsylvania", "pa"), ("Delaware", "de")],
        "nm": [("Colorado", "co"), ("Arizona", "az"), ("Texas", "tx"), ("Oklahoma", "ok"), ("Utah", "ut")],
        "ny": [("Vermont", "vt"), ("Massachusetts", "ma"), ("Connecticut", "ct"), ("New Jersey", "nj"), ("Pennsylvania", "pa")],
        "nc": [("Virginia", "va"), ("Tennessee", "tn"), ("Georgia", "ga"), ("South Carolina", "sc")],
        "nd": [("Minnesota", "mn"), ("South Dakota", "sd"), ("Montana", "mt")],
        "oh": [("Michigan", "mi"), ("Indiana", "in"), ("Kentucky", "ky"), ("West Virginia", "wv"), ("Pennsylvania", "pa")],
        "ok": [("Kansas", "ks"), ("Missouri", "mo"), ("Arkansas", "ar"), ("Texas", "tx"), ("New Mexico", "nm"), ("Colorado", "co")],
        "or": [("Washington", "wa"), ("Idaho", "id"), ("Nevada", "nv"), ("California", "ca")],
        "pa": [("New York", "ny"), ("New Jersey", "nj"), ("Delaware", "de"), ("Maryland", "md"), ("West Virginia", "wv"), ("Ohio", "oh")],
        "ri": [("Connecticut", "ct"), ("Massachusetts", "ma")],
        "sc": [("North Carolina", "nc"), ("Georgia", "ga")],
        "sd": [("North Dakota", "nd"), ("Minnesota", "mn"), ("Iowa", "ia"), ("Nebraska", "ne"), ("Wyoming", "wy"), ("Montana", "mt")],
        "tn": [("Kentucky", "ky"), ("Virginia", "va"), ("North Carolina", "nc"), ("Georgia", "ga"), ("Alabama", "al"), ("Mississippi", "ms"), ("Arkansas", "ar"), ("Missouri", "mo")],
        "tx": [("New Mexico", "nm"), ("Oklahoma", "ok"), ("Arkansas", "ar"), ("Louisiana", "la")],
        "ut": [("Idaho", "id"), ("Nevada", "nv"), ("Arizona", "az"), ("Colorado", "co"), ("New Mexico", "nm"), ("Wyoming", "wy")],
        "vt": [("New Hampshire", "nh"), ("Massachusetts", "ma"), ("New York", "ny")],
        "va": [("Maryland", "md"), ("West Virginia", "wv"), ("Kentucky", "ky"), ("Tennessee", "tn"), ("North Carolina", "nc")],
        "wa": [("Idaho", "id"), ("Oregon", "or")],
        "wv": [("Pennsylvania", "pa"), ("Maryland", "md"), ("Virginia", "va"), ("Kentucky", "ky"), ("Ohio", "oh")],
        "wi": [("Minnesota", "mn"), ("Iowa", "ia"), ("Illinois", "il"), ("Michigan", "mi")],
        "wy": [("Montana", "mt"), ("South Dakota", "sd"), ("Nebraska", "ne"), ("Colorado", "co"), ("Utah", "ut"), ("Idaho", "id")],
    }
    return neighbor_map.get(abbrev, [])


def rank_text(rate):
    sorted_rates = sorted([s["rate"] for s in STATES.values()])
    rank = sorted_rates.index(rate) + 1 if rate in sorted_rates else 25
    if rank <= 5:
        return f"one of the lowest in the nation (#{51-rank} lowest)"
    elif rank <= 15:
        return f"below the national average"
    elif rank <= 35:
        return f"near the national average"
    elif rank <= 45:
        return f"above the national average"
    else:
        return f"one of the highest in the nation"


def homestead(state):
    exemptions = {
        "Alabama": "$55,000 off assessed value for residents 65+; $5,000 for all others",
        "Alaska": "$54,000 exemption for seniors 65+",
        "Arizona": "Limited — some counties offer up to $3,500 off assessed value for seniors",
        "Arkansas": "$350 credit for homeowners; $425 for seniors",
        "California": "$7,000 off assessed value (Prop 13)",
        "Colorado": "Varies by county; typically exempts a portion of value",
        "Connecticut": "Varies by town; up to $1,000 off assessed value",
        "Delaware": "No statewide homestead exemption",
        "Florida": "$50,000 off assessed value ($25,000 for all homeowners + $25,000 for primary residence value $75K-$125K)",
        "Georgia": "$2,000-$4,000 off assessed value (varies by county)",
        "Hawaii": "No statewide homestead exemption",
        "Idaho": "Up to $125,000 exemption for homeowners 65+; $100,000 for others",
        "Illinois": "General homestead exemption up to $10,000 off equalized assessed value",
        "Indiana": "Supplemental homestead deduction and standard deduction",
        "Iowa": "Homestead tax credit = tax on first $4,850 of taxable value",
        "Kansas": "$20,000 exemption on appraised value for primary residence",
        "Kentucky": "Homestead exemption of $46,350 for 65+ and disabled (2026)",
        "Louisiana": "$7,500 exemption on assessed value",
        "Maine": "$25,000 exemption for residents 62+; varies by municipality",
        "Maryland": "Homestead Property Tax Credit caps annual increases at 10%",
        "Massachusetts": "Varies by municipality; residential exemption in some cities",
        "Michigan": "$54,000 (varies by community) for primary residence; 18 mills reduction",
        "Minnesota": "Homestead market value exclusion: 40% of first $76K",
        "Mississippi": "$7,500 exemption on assessed value for homeowners",
        "Missouri": "Varies by county; up to $1,500 credit in some areas",
        "Montana": "Up to 34% exemption on market value for primary residence (2026)",
        "Nebraska": "Homestead exemption for 65+, disabled, veterans — up to 100% exemption",
        "Nevada": "3% cap on annual tax increases for primary residence",
        "New Hampshire": "Low and moderate income homeowners tax credit",
        "New Jersey": "$25,000 deduction for 65+/disabled; $250 credit for others",
        "New Mexico": "$2,000 exemption on taxable value for homeowners",
        "New York": "STAR credit: $739-$1,531 for primary residence; Enhanced STAR for 65+",
        "North Carolina": "$25,000 or 50% (whichever is greater) exclusion for 65+",
        "North Dakota": "5% True and Full value reduction for homesteads",
        "Ohio": "Homestead exemption up to $26,200 off market value for 65+/disabled",
        "Oklahoma": "$1,000 homestead exemption on assessed value",
        "Oregon": "$23,842 (2026) exemption for seniors; varies by county for others",
        "Pennsylvania": "Varies by county; $95 homestead exclusion in some areas",
        "Rhode Island": "Varies by municipality",
        "South Carolina": "4% assessment ratio for owner-occupied (vs 6% for others)",
        "South Dakota": "$6,000 exemption on assessed value; 150% increase cap for seniors",
        "Tennessee": "Varies by county; up to $75,000 exemption in some areas",
        "Texas": "$25,000 exemption on appraised value for school taxes; 10% annual increase cap",
        "Utah": "45% exemption on primary residence value",
        "Vermont": "Property tax adjustment based on income for residents",
        "Virginia": "$25,000 exemption on assessed value for 65+/disabled",
        "Washington": "Varies; senior exemption up to $70,879 (2026)",
        "West Virginia": "$20,000 homestead exemption for 65+/disabled",
        "Wisconsin": "Lottery credit on primary residence; varies by municipality",
        "Wyoming": "$1,600 exemption on assessed value"
    }
    return exemptions.get(state, "Varies by county — check your local assessor's office")


def senior(state):
    return "Available in most counties — check your local assessor's office for specific amounts and age thresholds (typically 65+)"

def veteran(state):
    return "Disabled veterans (10%+ rating) may qualify for additional exemptions — varies by county. Contact your county assessor for details"

def disability(state):
    return "Disability exemptions available in most counties — typically mirrors the senior exemption. Contact your county assessor for specific amounts"


if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    site_dir = os.path.dirname(out_dir)
    
    for state, data in STATES.items():
        html = generate_page(state, data)
        filename = f"{data['abbrev']}-property-tax.html"
        filepath = os.path.join(site_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created {filename} ({len(html):,} bytes)")
    
    print(f"\nGenerated {len(STATES)} state property tax pages")

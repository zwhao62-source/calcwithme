#!/usr/bin/env python3
"""Generate 50 state closing cost pages and 50 state home insurance pages for CalcWithMe."""
import os

STATES = {
    "Alabama": {"abbrev": "al", "median_home": 170600, "closing_pct": 2.3, "avg_closing": 3920, "insurance_avg": 1840, "insurance_per_1k": 10.80},
    "Alaska": {"abbrev": "ak", "median_home": 331600, "closing_pct": 2.5, "avg_closing": 8290, "insurance_avg": 1280, "insurance_per_1k": 3.86},
    "Arizona": {"abbrev": "az", "median_home": 353500, "closing_pct": 2.1, "avg_closing": 7420, "insurance_avg": 2180, "insurance_per_1k": 6.17},
    "Arkansas": {"abbrev": "ar", "median_home": 193700, "closing_pct": 2.4, "avg_closing": 4650, "insurance_avg": 2520, "insurance_per_1k": 13.01},
    "California": {"abbrev": "ca", "median_home": 631200, "closing_pct": 1.8, "avg_closing": 11360, "insurance_avg": 1980, "insurance_per_1k": 3.14},
    "Colorado": {"abbrev": "co", "median_home": 490200, "closing_pct": 2.0, "avg_closing": 9800, "insurance_avg": 3420, "insurance_per_1k": 6.98},
    "Connecticut": {"abbrev": "ct", "median_home": 310800, "closing_pct": 2.8, "avg_closing": 8700, "insurance_avg": 2560, "insurance_per_1k": 8.24},
    "Delaware": {"abbrev": "de", "median_home": 314600, "closing_pct": 2.3, "avg_closing": 7240, "insurance_avg": 1020, "insurance_per_1k": 3.24},
    "Florida": {"abbrev": "fl", "median_home": 307400, "closing_pct": 2.5, "avg_closing": 7680, "insurance_avg": 4960, "insurance_per_1k": 16.14},
    "Georgia": {"abbrev": "ga", "median_home": 278400, "closing_pct": 2.2, "avg_closing": 6120, "insurance_avg": 2680, "insurance_per_1k": 9.63},
    "Hawaii": {"abbrev": "hi", "median_home": 755800, "closing_pct": 2.0, "avg_closing": 15120, "insurance_avg": 1480, "insurance_per_1k": 1.96},
    "Idaho": {"abbrev": "id", "median_home": 287100, "closing_pct": 2.1, "avg_closing": 6030, "insurance_avg": 1260, "insurance_per_1k": 4.39},
    "Illinois": {"abbrev": "il", "median_home": 241800, "closing_pct": 2.7, "avg_closing": 6530, "insurance_avg": 2140, "insurance_per_1k": 8.85},
    "Indiana": {"abbrev": "in", "median_home": 194300, "closing_pct": 2.2, "avg_closing": 4270, "insurance_avg": 1620, "insurance_per_1k": 8.34},
    "Iowa": {"abbrev": "ia", "median_home": 195500, "closing_pct": 2.3, "avg_closing": 4500, "insurance_avg": 1820, "insurance_per_1k": 9.31},
    "Kansas": {"abbrev": "ks", "median_home": 197100, "closing_pct": 2.2, "avg_closing": 4340, "insurance_avg": 2860, "insurance_per_1k": 14.51},
    "Kentucky": {"abbrev": "ky", "median_home": 188200, "closing_pct": 2.4, "avg_closing": 4520, "insurance_avg": 2640, "insurance_per_1k": 14.03},
    "Louisiana": {"abbrev": "la", "median_home": 209300, "closing_pct": 2.6, "avg_closing": 5440, "insurance_avg": 5260, "insurance_per_1k": 25.13},
    "Maine": {"abbrev": "me", "median_home": 277200, "closing_pct": 2.5, "avg_closing": 6930, "insurance_avg": 1180, "insurance_per_1k": 4.26},
    "Maryland": {"abbrev": "md", "median_home": 359600, "closing_pct": 2.4, "avg_closing": 8630, "insurance_avg": 1560, "insurance_per_1k": 4.34},
    "Massachusetts": {"abbrev": "ma", "median_home": 458800, "closing_pct": 2.8, "avg_closing": 12850, "insurance_avg": 1840, "insurance_per_1k": 4.01},
    "Michigan": {"abbrev": "mi", "median_home": 186400, "closing_pct": 2.3, "avg_closing": 4290, "insurance_avg": 2120, "insurance_per_1k": 11.37},
    "Minnesota": {"abbrev": "mn", "median_home": 299400, "closing_pct": 2.5, "avg_closing": 7490, "insurance_avg": 2480, "insurance_per_1k": 8.28},
    "Mississippi": {"abbrev": "ms", "median_home": 156800, "closing_pct": 2.5, "avg_closing": 3920, "insurance_avg": 3320, "insurance_per_1k": 21.17},
    "Missouri": {"abbrev": "mo", "median_home": 181800, "closing_pct": 2.2, "avg_closing": 4000, "insurance_avg": 2560, "insurance_per_1k": 14.08},
    "Montana": {"abbrev": "mt", "median_home": 295200, "closing_pct": 2.1, "avg_closing": 6200, "insurance_avg": 2140, "insurance_per_1k": 7.25},
    "Nebraska": {"abbrev": "ne", "median_home": 197200, "closing_pct": 2.3, "avg_closing": 4540, "insurance_avg": 2860, "insurance_per_1k": 14.50},
    "Nevada": {"abbrev": "nv", "median_home": 396300, "closing_pct": 2.0, "avg_closing": 7930, "insurance_avg": 1640, "insurance_per_1k": 4.14},
    "New Hampshire": {"abbrev": "nh", "median_home": 333200, "closing_pct": 2.6, "avg_closing": 8660, "insurance_avg": 1380, "insurance_per_1k": 4.14},
    "New Jersey": {"abbrev": "nj", "median_home": 387200, "closing_pct": 3.0, "avg_closing": 11620, "insurance_avg": 1520, "insurance_per_1k": 3.93},
    "New Mexico": {"abbrev": "nm", "median_home": 242600, "closing_pct": 2.2, "avg_closing": 5340, "insurance_avg": 2540, "insurance_per_1k": 10.47},
    "New York": {"abbrev": "ny", "median_home": 358700, "closing_pct": 3.2, "avg_closing": 11480, "insurance_avg": 1920, "insurance_per_1k": 5.35},
    "North Carolina": {"abbrev": "nc", "median_home": 221300, "closing_pct": 2.1, "avg_closing": 4650, "insurance_avg": 2240, "insurance_per_1k": 10.12},
    "North Dakota": {"abbrev": "nd", "median_home": 238300, "closing_pct": 2.2, "avg_closing": 5240, "insurance_avg": 2860, "insurance_per_1k": 12.00},
    "Ohio": {"abbrev": "oh", "median_home": 188300, "closing_pct": 2.4, "avg_closing": 4520, "insurance_avg": 1460, "insurance_per_1k": 7.75},
    "Oklahoma": {"abbrev": "ok", "median_home": 163200, "closing_pct": 2.3, "avg_closing": 3750, "insurance_avg": 4420, "insurance_per_1k": 27.08},
    "Oregon": {"abbrev": "or", "median_home": 371800, "closing_pct": 2.0, "avg_closing": 7440, "insurance_avg": 1240, "insurance_per_1k": 3.33},
    "Pennsylvania": {"abbrev": "pa", "median_home": 224600, "closing_pct": 2.6, "avg_closing": 5840, "insurance_avg": 1480, "insurance_per_1k": 6.59},
    "Rhode Island": {"abbrev": "ri", "median_home": 301300, "closing_pct": 2.7, "avg_closing": 8140, "insurance_avg": 2040, "insurance_per_1k": 6.77},
    "South Carolina": {"abbrev": "sc", "median_home": 212700, "closing_pct": 2.3, "avg_closing": 4890, "insurance_avg": 2840, "insurance_per_1k": 13.35},
    "South Dakota": {"abbrev": "sd", "median_home": 204500, "closing_pct": 2.2, "avg_closing": 4500, "insurance_avg": 2580, "insurance_per_1k": 12.62},
    "Tennessee": {"abbrev": "tn", "median_home": 234000, "closing_pct": 2.2, "avg_closing": 5150, "insurance_avg": 2620, "insurance_per_1k": 11.20},
    "Texas": {"abbrev": "tx", "median_home": 252100, "closing_pct": 2.5, "avg_closing": 6300, "insurance_avg": 4460, "insurance_per_1k": 17.69},
    "Utah": {"abbrev": "ut", "median_home": 412800, "closing_pct": 2.0, "avg_closing": 8260, "insurance_avg": 1260, "insurance_per_1k": 3.05},
    "Vermont": {"abbrev": "vt", "median_home": 257300, "closing_pct": 2.6, "avg_closing": 6690, "insurance_avg": 1280, "insurance_per_1k": 4.98},
    "Virginia": {"abbrev": "va", "median_home": 302400, "closing_pct": 2.2, "avg_closing": 6650, "insurance_avg": 1680, "insurance_per_1k": 5.56},
    "Washington": {"abbrev": "wa", "median_home": 426400, "closing_pct": 1.9, "avg_closing": 8100, "insurance_avg": 1360, "insurance_per_1k": 3.19},
    "West Virginia": {"abbrev": "wv", "median_home": 170700, "closing_pct": 2.4, "avg_closing": 4100, "insurance_avg": 2020, "insurance_per_1k": 11.83},
    "Wisconsin": {"abbrev": "wi", "median_home": 220100, "closing_pct": 2.4, "avg_closing": 5280, "insurance_avg": 1480, "insurance_per_1k": 6.72},
    "Wyoming": {"abbrev": "wy", "median_home": 265300, "closing_pct": 2.1, "avg_closing": 5570, "insurance_avg": 2080, "insurance_per_1k": 7.84}
}


def generate_closing_cost_page(state, data):
    ab = data["abbrev"]
    median = data["median_home"]
    close_pct = data["closing_pct"]
    avg_close = data["avg_closing"]

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{state} Closing Cost Calculator 2026 - Average ${avg_close:,} | CalcWithMe</title>
    <meta name="description" content="{state} closing cost calculator 2026. Average closing costs ${avg_close:,} ({close_pct}% of home price). Calculate your exact fees for {state} home purchase.">
    <meta name="keywords" content="{state} closing costs, {ab} closing cost calculator, {state} home closing fees">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://calcwithme.com/{ab}-closing-costs.html">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📋</text></svg>">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://calcwithme.com/"}},
      {{"@type":"ListItem","position":2,"name":"Closing Costs by State","item":"https://calcwithme.com/closing-cost-calculator.html"}},
      {{"@type":"ListItem","position":3,"name":"{state}","item":"https://calcwithme.com/{ab}-closing-costs.html"}}
    ]}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {{"@type":"Question","name":"What are average closing costs in {state}?","acceptedAnswer":{{"@type":"Answer","text":"Average closing costs in {state} are ${avg_close:,} ({close_pct}% of the median home price of ${median:,}). This includes lender fees, title insurance, appraisal, and {state}-specific fees."}}}}
    ]}}
    </script>
    <script defer src="https://cloud.umami.is/script.js" data-website-id="77de646f-0376-43ee-8b45-326250fd1485"></script>
</head>
<body>
    <header><div class="container header-inner"><a href="/" class="logo"><span class="logo-icon">&#x1F522;</span><span>Calc<span class="highlight">With</span>Me</span></a><nav><a href="/#calculators">Calculators</a><a href="/#about">About</a><a href="/blog">Blog</a><a href="/savings-tips.html">&#x1F4B0; Money Tips</a><a href="/mortgage-calculator.html">Mortgage</a></nav></div></header>
    <main class="calculator-page"><div class="container"><div class="calculator-layout"><div class="calculator-main">
        <h1>{state} Closing Cost Calculator 2026</h1>
        <p class="page-desc">Average closing costs in {state}: <strong>${avg_close:,} ({close_pct}% of home price)</strong>. Calculate your exact fees. Updated June 2026.</p>
        <div class="calc-form">
            <div class="form-group"><label for="ccHome">Home Price in {state}</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="ccHome" class="has-prefix" value="{median}" min="0"></div></div>
            <div class="form-group"><label for="ccDown">Down Payment</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="ccDown" class="has-prefix" value="{round(median*0.2)}" min="0"></div></div>
            <button class="btn-calculate" onclick="calcCC()">Calculate {state} Closing Costs</button>
        </div>
        <div class="ad-container">Advertisement Space</div>
        <div class="calc-content">
            <h2>{state} Closing Cost Overview</h2>
            <p>{state} closing costs average <strong>${avg_close:,}</strong> on a median-priced home of ${median:,}. This represents {close_pct}% of the purchase price. {state} ranks {rank_closing(close_pct)} among all states for closing cost burden.</p>
            <ul>
                <li><strong>Average closing costs:</strong> ${avg_close:,}</li>
                <li><strong>As % of home price:</strong> {close_pct}%</li>
                <li><strong>Median home value:</strong> ${median:,}</li>
                <li><strong>Who typically pays:</strong> Buyer pays most fees; seller pays transfer tax and realtor commissions in {state}</li>
            </ul>
            <h2>{state} Closing Cost Breakdown</h2>
            <ul>
                <li><strong>Lender origination fee:</strong> 0.5-1% of loan amount</li>
                <li><strong>Appraisal:</strong> $300-$600</li>
                <li><strong>Title insurance (lender):</strong> $500-$1,500</li>
                <li><strong>Title search:</strong> $200-$400</li>
                <li><strong>Attorney fees:</strong> {"$500-$1,500 (required in some {state} transactions)" if close_pct >= 2.5 else "$0-$500 (not typically required in {state})"}</li>
                <li><strong>Recording fee:</strong> $25-$150</li>
                <li><strong>Survey:</strong> $200-$500</li>
                <li><strong>Inspection:</strong> $300-$500</li>
                <li><strong>Transfer tax:</strong> {transfer_tax(state)}</li>
                <li><strong>Prepaid items:</strong> Property tax escrow + homeowner's insurance (2-6 months upfront)</li>
            </ul>
            <h2>How to Reduce {state} Closing Costs</h2>
            <ul>
                <li><strong>Shop lenders:</strong> Closing costs vary 30-50% between lenders. Get at least 3 Loan Estimates.</li>
                <li><strong>Negotiate:</strong> Ask the seller to cover up to {seller_concession(state)} in closing costs (seller concessions).</li>
                <li><strong>Lender credits:</strong> Accept a slightly higher rate in exchange for lower upfront fees (good if you plan to refinance).</li>
                <li><strong>Compare title insurance:</strong> You can shop for title insurance — don't just accept the lender's provider.</li>
                <li><strong>Close at month-end:</strong> Reduces prepaid interest — can save $500-$1,000.</li>
                <li><strong>Negotiate realtor commission:</strong> Post-NAR settlement (2025), commissions are negotiable and not automatically paid by seller.</li>
            </ul>
            <h2>{state}-Specific Closing Cost Rules</h2>
            <ul>{state_rules(state)}</ul>
            <div class="related-calcs"><h3>Related Calculators</h3><a href="closing-cost-calculator.html">Closing Cost Calculator</a><a href="mortgage-calculator.html">Mortgage</a><a href="property-tax-calculator.html">Property Tax</a><a href="{ab}-first-time-home-buyer.html">{state} First-Time Buyer</a></div>
        </div>
        <div class="faq-section"><h3>Frequently Asked Questions</h3>
            <details class="faq-item"><summary>What are average closing costs in {state}?</summary><p>Average closing costs in {state} are ${avg_close:,} ({close_pct}% of the median home price of ${median:,}). This includes lender fees, title insurance, appraisal, and {state}-specific fees.</p></details>
            <details class="faq-item"><summary>Who pays closing costs in {state}?</summary><p>Buyers typically pay 2-5% of the home price in closing costs. Sellers pay realtor commissions and transfer taxes. In {state}, buyers can ask sellers for concessions up to {seller_concession(state)} of the purchase price.</p></details>
        </div>
    </div>
    <aside class="results-panel">
        <h2>&#x1F4CA; {state} Closing Costs</h2>
        <div class="result-item"><p class="result-label">Estimated Total</p><p class="result-value" id="ccTotal" style="color:#2563eb;">$0</p></div>
        <div class="result-item"><p class="result-label">% of Home Price</p><p class="result-value" id="ccPct" style="color:#f59e0b;">0%</p></div>
        <div class="results-breakdown">
            <h3 style="font-size:0.95rem;font-weight:700;margin-bottom:12px;">Fee Breakdown</h3>
            <div class="breakdown-row"><span>Lender Fees</span><span id="ccLender">$0</span></div>
            <div class="breakdown-row"><span>Title & Escrow</span><span id="ccTitle">$0</span></div>
            <div class="breakdown-row"><span>Government Fees</span><span id="ccGov">$0</span></div>
            <div class="breakdown-row"><span>Prepaids</span><span id="ccPrepaid">$0</span></div>
        </div>
    </aside></div></div></main>
    <footer><div class="container"><div class="footer-inner"><div class="footer-brand"><span class="logo-icon">&#x1F522;</span><span>CalcWithMe</span><p>Free financial calculators.</p></div><div class="footer-links"><h4>Popular</h4><a href="mortgage-calculator.html">Mortgage</a><a href="loan-calculator.html">Loan</a><a href="compound-interest-calculator.html">Compound Interest</a></div><div class="footer-links"><h4>More</h4><a href="auto-loan-calculator.html">Auto Loan</a><a href="retirement-calculator.html">Retirement</a><a href="salary-calculator.html">Salary</a></div></div><div class="footer-bottom"><p>&#169; 2026 CalcWithMe.com.</p></div></div></footer>
    <script>
    function calcCC() {{
        const home = parseFloat(document.getElementById('ccHome').value) || 0;
        const down = parseFloat(document.getElementById('ccDown').value) || 0;
        const loan = home - down;
        const rate = {close_pct}/100;
        const total = home * rate;
        const lender = loan * 0.008;
        const title = home * 0.006;
        const gov = home * 0.003;
        const prepaid = home * 0.005;
        const fmt = v => '$' + Math.round(v).toLocaleString();
        document.getElementById('ccTotal').textContent = fmt(total);
        document.getElementById('ccPct').textContent = (rate*100).toFixed(1) + '%';
        document.getElementById('ccLender').textContent = fmt(lender);
        document.getElementById('ccTitle').textContent = fmt(title);
        document.getElementById('ccGov').textContent = fmt(gov);
        document.getElementById('ccPrepaid').textContent = fmt(prepaid);
    }}
    window.addEventListener('load', calcCC);
    </script>
    <div class="visitor-counter"><span>👁️ Visitors: </span><span id="visitor-counter" style="display:none;">0</span></div>
    <script src="js/visitor-counter.js"></script>
</body></html>'''


def generate_home_insurance_page(state, data):
    ab = data["abbrev"]
    median = data["median_home"]
    ins_avg = data["insurance_avg"]
    ins_per_1k = data["insurance_per_1k"]

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{state} Home Insurance Calculator 2026 - Average ${ins_avg:,}/yr | CalcWithMe</title>
    <meta name="description" content="{state} home insurance calculator 2026. Average annual premium ${ins_avg:,} (${ins_per_1k:.2f} per $1K coverage). Compare rates and find savings. Updated June 2026.">
    <meta name="keywords" content="{state} home insurance, {ab} homeowners insurance, {state} home insurance rates, {state} home insurance calculator">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://calcwithme.com/{ab}-home-insurance.html">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🛡️</text></svg>">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://calcwithme.com/"}},
      {{"@type":"ListItem","position":2,"name":"Home Insurance by State","item":"https://calcwithme.com/home-insurance-calculator.html"}},
      {{"@type":"ListItem","position":3,"name":"{state}","item":"https://calcwithme.com/{ab}-home-insurance.html"}}
    ]}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {{"@type":"Question","name":"How much is home insurance in {state}?","acceptedAnswer":{{"@type":"Answer","text":"Average home insurance in {state} costs ${ins_avg:,}/year or ${round(ins_avg/12)}/month. That's ${ins_per_1k:.2f} per $1,000 of coverage on a median home value of ${median:,}."}}}}
    ]}}
    </script>
    <script defer src="https://cloud.umami.is/script.js" data-website-id="77de646f-0376-43ee-8b45-326250fd1485"></script>
</head>
<body>
    <header><div class="container header-inner"><a href="/" class="logo"><span class="logo-icon">&#x1F522;</span><span>Calc<span class="highlight">With</span>Me</span></a><nav><a href="/#calculators">Calculators</a><a href="/#about">About</a><a href="/blog">Blog</a><a href="/savings-tips.html">&#x1F4B0; Money Tips</a><a href="/mortgage-calculator.html">Mortgage</a></nav></div></header>
    <main class="calculator-page"><div class="container"><div class="calculator-layout"><div class="calculator-main">
        <h1>{state} Home Insurance Calculator 2026</h1>
        <p class="page-desc">Average {state} home insurance: <strong>${ins_avg:,}/year (${round(ins_avg/12)}/month)</strong>. ${ins_per_1k:.2f} per $1K coverage. Updated June 2026.</p>
        <div class="calc-form">
            <div class="form-group"><label for="hiHome">Dwelling Coverage Amount</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="hiHome" class="has-prefix" value="{median}" min="0"></div></div>
            <div class="form-group"><label>Deductible</label><select id="hiDed"><option value="500">$500</option><option value="1000" selected>$1,000</option><option value="2000">$2,000</option><option value="5000">$5,000</option></select></div>
            <button class="btn-calculate" onclick="calcHI()">Calculate {state} Home Insurance</button>
        </div>
        <div class="ad-container">Advertisement Space</div>
        <div class="calc-content">
            <h2>{state} Home Insurance Overview</h2>
            <p>{state} homeowners insurance averages <strong>${ins_avg:,}/year</strong> (${round(ins_avg/12)}/month), which is {ins_vs_national(ins_avg)} the national average of $2,230/year. {state} rates are {rate_reason(state)}.</p>
            <ul>
                <li><strong>Average annual premium:</strong> ${ins_avg:,}</li>
                <li><strong>Average monthly:</strong> ${round(ins_avg/12)}</li>
                <li><strong>Per $1,000 coverage:</strong> ${ins_per_1k:.2f}</li>
                <li><strong>Median home value:</strong> ${median:,}</li>
                <li><strong>{state} rank:</strong> #{ins_rank(state)} most expensive state</li>
            </ul>
            <h2>What {state} Home Insurance Covers</h2>
            <ul>
                <li><strong>Dwelling:</strong> Physical structure of your home and attached structures</li>
                <li><strong>Other structures:</strong> Detached garage, shed, fence (typically 10% of dwelling coverage)</li>
                <li><strong>Personal property:</strong> Furniture, electronics, clothing (50-70% of dwelling)</li>
                <li><strong>Loss of use:</strong> Hotel and living expenses if home is uninhabitable (20-30% of dwelling)</li>
                <li><strong>Liability:</strong> Legal protection if someone is injured on your property ($100K-$300K standard)</li>
                <li><strong>Medical payments:</strong> Small medical bills for guests injured on your property ($1K-$5K)</li>
            </ul>
            <h2>{state}-Specific Insurance Risks</h2>
            <ul>{state_risks(state)}</ul>
            <h2>How to Save on {state} Home Insurance</h2>
            <ul>
                <li><strong>Bundle home + auto:</strong> Save 10-25% on both policies with the same insurer</li>
                <li><strong>Raise your deductible:</strong> Going from $500 to $2,000 deductible can save 15-25%</li>
                <li><strong>Improve home security:</strong> Alarm systems, deadbolts, and smoke detectors save 5-15%</li>
                <li><strong>Maintain good credit:</strong> In most states, credit score impacts insurance rates significantly</li>
                <li><strong>Stay claim-free:</strong> 3-5 years without a claim earns a 10-20% discount</li>
                <li><strong>Shop every 2 years:</strong> Rates change constantly. Get 3-5 quotes each renewal cycle</li>
                <li><strong>Ask about {state} discounts:</strong> New roof, impact-resistant roofing, wind mitigation, loyalty</li>
            </ul>
            <div class="related-calcs"><h3>Related Calculators</h3><a href="home-affordability-calculator.html">Home Affordability</a><a href="mortgage-calculator.html">Mortgage</a><a href="property-tax-calculator.html">Property Tax</a><a href="{ab}-closing-costs.html">{state} Closing Costs</a></div>
        </div>
        <div class="faq-section"><h3>Frequently Asked Questions</h3>
            <details class="faq-item"><summary>How much is home insurance in {state}?</summary><p>Average home insurance in {state} costs ${ins_avg:,}/year or ${round(ins_avg/12)}/month. That's ${ins_per_1k:.2f} per $1,000 of coverage. Rates vary by location, home age, and coverage level.</p></details>
            <details class="faq-item"><summary>Is home insurance required in {state}?</summary><p>{state} law does not require homeowners insurance, but your mortgage lender will require it. Even without a mortgage, insurance protects your largest asset from fire, storms, theft, and liability.</p></details>
        </div>
    </div>
    <aside class="results-panel">
        <h2>&#x1F4CA; {state} Insurance</h2>
        <div class="result-item"><p class="result-label">Annual Premium (est.)</p><p class="result-value" id="hiAnnual" style="color:#2563eb;">$0</p></div>
        <div class="result-item"><p class="result-label">Monthly Premium</p><p class="result-value" id="hiMonthly" style="color:#16a34a;">$0</p></div>
        <div class="result-item"><p class="result-label">Per $1K Coverage</p><p class="result-value" id="hiPer1k">${ins_per_1k:.2f}</p></div>
        <div class="results-breakdown">
            <h3 style="font-size:0.95rem;font-weight:700;margin-bottom:12px;">Coverage Estimates</h3>
            <div class="breakdown-row"><span>Dwelling</span><span id="hiDwell">$0</span></div>
            <div class="breakdown-row"><span>Personal Property</span><span id="hiPers">$0</span></div>
            <div class="breakdown-row"><span>Liability</span><span id="hiLiab">$300K</span></div>
            <div class="breakdown-row"><span>Loss of Use</span><span id="hiLoss">$0</span></div>
        </div>
    </aside></div></div></main>
    <footer><div class="container"><div class="footer-inner"><div class="footer-brand"><span class="logo-icon">&#x1F522;</span><span>CalcWithMe</span><p>Free financial calculators.</p></div><div class="footer-links"><h4>Popular</h4><a href="mortgage-calculator.html">Mortgage</a><a href="loan-calculator.html">Loan</a><a href="compound-interest-calculator.html">Compound Interest</a></div><div class="footer-links"><h4>More</h4><a href="auto-loan-calculator.html">Auto Loan</a><a href="retirement-calculator.html">Retirement</a><a href="salary-calculator.html">Salary</a></div></div><div class="footer-bottom"><p>&#169; 2026 CalcWithMe.com.</p></div></div></footer>
    <script>
    function calcHI() {{
        const home = parseFloat(document.getElementById('hiHome').value) || 0;
        const ded = parseFloat(document.getElementById('hiDed').value) || 1000;
        const rate = {ins_per_1k}/1000;
        let premium = home * rate;
        if (ded >= 2000) premium *= 0.82;
        else if (ded >= 1000) premium *= 0.92;
        const fmt = v => '$' + Math.round(v).toLocaleString();
        document.getElementById('hiAnnual').textContent = fmt(premium);
        document.getElementById('hiMonthly').textContent = fmt(premium/12);
        document.getElementById('hiDwell').textContent = fmt(home);
        document.getElementById('hiPers').textContent = fmt(home * 0.6);
        document.getElementById('hiLoss').textContent = fmt(home * 0.2);
    }}
    window.addEventListener('load', calcHI);
    </script>
    <div class="visitor-counter"><span>👁️ Visitors: </span><span id="visitor-counter" style="display:none;">0</span></div>
    <script src="js/visitor-counter.js"></script>
</body></html>'''


def rank_closing(pct):
    if pct <= 2.0: return "among the lowest"
    elif pct <= 2.3: return "below average"
    elif pct <= 2.6: return "near average"
    else: return "above average"

def transfer_tax(state):
    if state in ["New York", "New Jersey", "Connecticut", "Maryland", "Delaware", "Pennsylvania"]:
        return f"Varies by county — {state} has a state transfer tax of 0.5-2%"
    elif state in ["Texas", "Florida", "California"]:
        return f"Typically paid by seller in {state} — $1-$2 per $1,000 of sale price"
    else:
        return f"Minimal or no state transfer tax in {state} — typically $1-$5 per $1,000"

def seller_concession(state):
    if state in ["California", "New York", "Massachusetts"]: return "3-6%"
    elif state in ["Texas", "Florida"]: return "up to 6%"
    else: return "3-6%"

def state_rules(state):
    rules = {
        "New York": "<li><strong>Mortgage recording tax:</strong> 1.05-1.8% of mortgage amount (varies by county)</li><li><strong>Title insurance rates:</strong> Regulated by the state — less variation between providers</li><li><strong>Attorney required:</strong> Yes — both buyer and seller must have attorneys in NYC area</li>",
        "New Jersey": "<li><strong>Mansion tax:</strong> 1% surcharge on homes over $1,000,000</li><li><strong>Realty transfer fee:</strong> Progressive rate based on sale price</li><li><strong>Attorney recommended:</strong> Common but not required by state law</li>",
        "Florida": "<li><strong>Documentary stamp tax:</strong> $0.70 per $100 of sale price</li><li><strong>Intangible tax on mortgage:</strong> $0.002 per dollar of new mortgage</li><li><strong>Title insurance:</strong> Promulgated (set) rates — less room to negotiate</li>",
        "Texas": "<li><strong>No state income tax:</strong> Property taxes are higher to compensate</li><li><strong>Seller pays title insurance:</strong> Customary in most Texas markets</li><li><strong>Option fee:</strong> $100-$500 for exclusive right to terminate during option period</li>",
        "California": "<li><strong>Transfer tax:</strong> $1.10 per $1,000 (may be higher in some cities)</li><li><strong>Escrow companies:</strong> Common instead of attorneys for closing</li><li><strong>Mello-Roos:</strong> Special tax districts — check if the home is in one</li>",
    }
    return rules.get(state, f"<li><strong>Standard closing process</strong> in {state} — attorney not typically required</li><li><strong>Transfer tax:</strong> Check your county for local rates</li><li><strong>Title insurance:</strong> Shop around — rates vary by provider in {state}</li>")

def ins_vs_national(avg):
    if avg > 3000: return "well above"
    elif avg > 2300: return "above"
    elif avg > 1800: return "near"
    elif avg > 1400: return "below"
    else: return "well below"

def rate_reason(state):
    if state in ["Florida", "Louisiana"]: return "driven by hurricane and flood risk"
    elif state in ["Texas", "Oklahoma"]: return "driven by tornado and hail risk"
    elif state in ["Mississippi", "Alabama"]: return "driven by severe weather risk"
    elif state in ["California"]: return "driven by wildfire risk, though rates are partially regulated"
    elif state in ["Kansas", "Nebraska", "South Dakota", "North Dakota"]: return "driven by tornado and wind risk"
    elif state in ["Hawaii", "Oregon", "Washington"]: return "moderate due to lower natural disaster risk"
    else: return "moderate compared to the national average"

def ins_rank(state):
    sorted_states = sorted(STATES.items(), key=lambda x: x[1]["insurance_avg"], reverse=True)
    for i, (s, _) in enumerate(sorted_states):
        if s == state: return i + 1
    return 25

def state_risks(state):
    if state in ["Florida", "Louisiana"]: return "<li><strong>Hurricanes:</strong> Major risk — wind and flood damage. Separate flood insurance required (FEMA NFIP or private)</li><li><strong>Flood zones:</strong> Check FEMA flood maps — flood insurance is NOT included in standard policies</li><li><strong>Wind mitigation:</strong> {state} offers discounts for hurricane shutters, impact windows, and roof-to-wall connections</li>"
    elif state in ["Texas", "Oklahoma", "Kansas"]: return "<li><strong>Tornadoes:</strong> High risk — ensure your policy covers wind damage</li><li><strong>Hail:</strong> Frequent claims — consider impact-resistant roofing for discounts</li><li><strong>Wildfire:</strong> Western {state} areas face increasing wildfire risk</li>"
    elif state in ["California"]: return "<li><strong>Wildfire:</strong> High risk in many areas — FAIR Plan available if insurers won't cover you</li><li><strong>Earthquake:</strong> Not covered by standard insurance — separate earthquake policy needed</li><li><strong>Landslide:</strong> Often excluded — check your policy carefully</li>"
    elif state in ["Mississippi", "Alabama", "South Carolina", "Georgia"]: return "<li><strong>Severe storms:</strong> Tornadoes and thunderstorms with hail and wind damage</li><li><strong>Hurricanes:</strong> Gulf Coast areas at risk for storm surge and wind damage</li><li><strong>Flood:</strong> Not covered by standard policies — check FEMA flood zone designation</li>"
    else: return "<li><strong>Severe weather:</strong> Thunderstorms, wind, and hail are the most common claims</li><li><strong>Winter storms:</strong> Pipe bursts and ice dams in colder months</li><li><strong>Water damage:</strong> Most common claim type nationally — check plumbing coverage</li>"


if __name__ == "__main__":
    site_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    for state, data in STATES.items():
        # Closing cost page
        html = generate_closing_cost_page(state, data)
        fname = f"{data['abbrev']}-closing-costs.html"
        with open(os.path.join(site_dir, fname), 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created {fname} ({len(html):,} bytes)")
        
        # Home insurance page
        html2 = generate_home_insurance_page(state, data)
        fname2 = f"{data['abbrev']}-home-insurance.html"
        with open(os.path.join(site_dir, fname2), 'w', encoding='utf-8') as f:
            f.write(html2)
        print(f"  Created {fname2} ({len(html2):,} bytes)")
    
    print(f"\nGenerated {len(STATES)*2} state pages ({len(STATES)} closing cost + {len(STATES)} home insurance)")

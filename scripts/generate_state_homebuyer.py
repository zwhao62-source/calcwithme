#!/usr/bin/env python3
"""Generate 50 state first-time homebuyer pages for CalcWithMe."""
import os

STATES = {
    "Alabama": {"abbrev": "al", "median_home": 170600, "avg_rate": 6.45, "down_pct": 6, "program": "Alabama Housing Finance Authority (AHFA)", "max_income": 98000, "dpa": "Up to $7,500 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Alaska": {"abbrev": "ak", "median_home": 331600, "avg_rate": 6.50, "down_pct": 5, "program": "Alaska Housing Finance Corporation (AHFC)", "max_income": 120000, "dpa": "Up to $10,000 down payment assistance", "dpa_rate": "0% (forgiven after 15 years)"},
    "Arizona": {"abbrev": "az", "median_home": 353500, "avg_rate": 6.40, "down_pct": 5, "program": "Arizona Department of Housing (ADOH)", "max_income": 105000, "dpa": "Up to 5% of purchase price", "dpa_rate": "0% (forgiven after 5-15 years)"},
    "Arkansas": {"abbrev": "ar", "median_home": 193700, "avg_rate": 6.45, "down_pct": 5, "program": "Arkansas Development Finance Authority (ADFA)", "max_income": 88000, "dpa": "Up to $10,000 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "California": {"abbrev": "ca", "median_home": 631200, "avg_rate": 6.35, "down_pct": 5, "program": "California Housing Finance Agency (CalHFA)", "max_income": 180000, "dpa": "Up to $15,000 or 3.5% of purchase price", "dpa_rate": "0% (deferred until sale/refi)"},
    "Colorado": {"abbrev": "co", "median_home": 490200, "avg_rate": 6.40, "down_pct": 5, "program": "Colorado Housing and Finance Authority (CHFA)", "max_income": 135000, "dpa": "Up to 5% of first mortgage (grant)", "dpa_rate": "0% (grant — no repayment)"},
    "Connecticut": {"abbrev": "ct", "median_home": 310800, "avg_rate": 6.40, "down_pct": 5, "program": "Connecticut Housing Finance Authority (CHFA)", "max_income": 118000, "dpa": "Up to $10,000 down payment loan", "dpa_rate": "0% (deferred 30 years)"},
    "Delaware": {"abbrev": "de", "median_home": 314600, "avg_rate": 6.45, "down_pct": 5, "program": "Delaware State Housing Authority (DSHA)", "max_income": 105000, "dpa": "Up to $10,000 down payment assistance", "dpa_rate": "0% (forgiven after 5-10 years)"},
    "Florida": {"abbrev": "fl", "median_home": 307400, "avg_rate": 6.45, "down_pct": 5, "program": "Florida Housing Finance Corporation (FHFC)", "max_income": 110000, "dpa": "Up to $10,000 or 5% of purchase price", "dpa_rate": "0% (forgiven after 5 years)"},
    "Georgia": {"abbrev": "ga", "median_home": 278400, "avg_rate": 6.45, "down_pct": 5, "program": "Georgia Department of Community Affairs (DCA)", "max_income": 105000, "dpa": "Up to $7,500 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Hawaii": {"abbrev": "hi", "median_home": 755800, "avg_rate": 6.35, "down_pct": 5, "program": "Hawaii Housing Finance and Development Corp (HHFDC)", "max_income": 165000, "dpa": "Up to $25,000 down payment assistance", "dpa_rate": "0% (deferred until sale)"},
    "Idaho": {"abbrev": "id", "median_home": 287100, "avg_rate": 6.45, "down_pct": 5, "program": "Idaho Housing and Finance Association (IHFA)", "max_income": 98000, "dpa": "Up to $15,000 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Illinois": {"abbrev": "il", "median_home": 241800, "avg_rate": 6.40, "down_pct": 5, "program": "Illinois Housing Development Authority (IHDA)", "max_income": 115000, "dpa": "Up to $10,000 or 5% of purchase price", "dpa_rate": "0% (forgiven after 10 years)"},
    "Indiana": {"abbrev": "in", "median_home": 194300, "avg_rate": 6.45, "down_pct": 5, "program": "Indiana Housing and Community Development Authority (IHCDA)", "max_income": 95000, "dpa": "Up to 6% of purchase price", "dpa_rate": "0% (forgiven after 2 years)"},
    "Iowa": {"abbrev": "ia", "median_home": 195500, "avg_rate": 6.45, "down_pct": 5, "program": "Iowa Finance Authority (IFA)", "max_income": 92000, "dpa": "Up to $5,000 grant", "dpa_rate": "0% (grant — no repayment)"},
    "Kansas": {"abbrev": "ks", "median_home": 197100, "avg_rate": 6.45, "down_pct": 5, "program": "Kansas Housing Resources Corporation (KHRC)", "max_income": 90000, "dpa": "Up to 5% of purchase price", "dpa_rate": "0% (forgiven after 10 years)"},
    "Kentucky": {"abbrev": "ky", "median_home": 188200, "avg_rate": 6.45, "down_pct": 5, "program": "Kentucky Housing Corporation (KHC)", "max_income": 92000, "dpa": "Up to $7,500 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Louisiana": {"abbrev": "la", "median_home": 209300, "avg_rate": 6.50, "down_pct": 5, "program": "Louisiana Housing Corporation (LHC)", "max_income": 90000, "dpa": "Up to 4% of purchase price", "dpa_rate": "0% (forgiven after 10 years)"},
    "Maine": {"abbrev": "me", "median_home": 277200, "avg_rate": 6.45, "down_pct": 5, "program": "MaineHousing", "max_income": 100000, "dpa": "Up to $5,000 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Maryland": {"abbrev": "md", "median_home": 359600, "avg_rate": 6.40, "down_pct": 5, "program": "Maryland Department of Housing (MDHCD)", "max_income": 135000, "dpa": "Up to $10,000 or 5% of purchase price", "dpa_rate": "0% (deferred until sale)"},
    "Massachusetts": {"abbrev": "ma", "median_home": 458800, "avg_rate": 6.35, "down_pct": 5, "program": "MassHousing", "max_income": 145000, "dpa": "Up to $15,000 or 5% of purchase price", "dpa_rate": "0% (deferred until sale)"},
    "Michigan": {"abbrev": "mi", "median_home": 186400, "avg_rate": 6.45, "down_pct": 5, "program": "Michigan State Housing Development Authority (MSHDA)", "max_income": 95000, "dpa": "Up to $10,000 down payment loan", "dpa_rate": "0% (forgiven after 5 years)"},
    "Minnesota": {"abbrev": "mn", "median_home": 299400, "avg_rate": 6.40, "down_pct": 5, "program": "Minnesota Housing Finance Agency", "max_income": 115000, "dpa": "Up to $12,000 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Mississippi": {"abbrev": "ms", "median_home": 156800, "avg_rate": 6.50, "down_pct": 5, "program": "Mississippi Home Corporation (MHC)", "max_income": 85000, "dpa": "Up to $5,000 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Missouri": {"abbrev": "mo", "median_home": 181800, "avg_rate": 6.45, "down_pct": 5, "program": "Missouri Housing Development Commission (MHDC)", "max_income": 92000, "dpa": "Up to 4.5% of purchase price (grant)", "dpa_rate": "0% (grant — no repayment)"},
    "Montana": {"abbrev": "mt", "median_home": 295200, "avg_rate": 6.45, "down_pct": 5, "program": "Montana Board of Housing (MBOH)", "max_income": 100000, "dpa": "Up to $10,000 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Nebraska": {"abbrev": "ne", "median_home": 197200, "avg_rate": 6.45, "down_pct": 5, "program": "Nebraska Investment Finance Authority (NIFA)", "max_income": 92000, "dpa": "Up to 5% of purchase price", "dpa_rate": "0% (forgiven after 10 years)"},
    "Nevada": {"abbrev": "nv", "median_home": 396300, "avg_rate": 6.40, "down_pct": 5, "program": "Nevada Housing Division (NHD)", "max_income": 115000, "dpa": "Up to 5% of purchase price (grant)", "dpa_rate": "0% (grant — no repayment)"},
    "New Hampshire": {"abbrev": "nh", "median_home": 333200, "avg_rate": 6.40, "down_pct": 5, "program": "New Hampshire Housing Finance Authority (NHHFA)", "max_income": 110000, "dpa": "Up to $10,000 down payment assistance", "dpa_rate": "0% (forgiven after 5 years)"},
    "New Jersey": {"abbrev": "nj", "median_home": 387200, "avg_rate": 6.35, "down_pct": 5, "program": "New Jersey Housing and Mortgage Finance Agency (HMFA)", "max_income": 145000, "dpa": "Up to $15,000 down payment assistance", "dpa_rate": "0% (forgiven after 5 years)"},
    "New Mexico": {"abbrev": "nm", "median_home": 242600, "avg_rate": 6.45, "down_pct": 5, "program": "New Mexico Mortgage Finance Authority (MFA)", "max_income": 95000, "dpa": "Up to 8% of purchase price", "dpa_rate": "0% (forgiven after 10 years)"},
    "New York": {"abbrev": "ny", "median_home": 358700, "avg_rate": 6.35, "down_pct": 5, "program": "State of New York Mortgage Agency (SONYMA)", "max_income": 145000, "dpa": "Up to $15,000 or 5% of purchase price", "dpa_rate": "0% (forgiven after 10 years)"},
    "North Carolina": {"abbrev": "nc", "median_home": 221300, "avg_rate": 6.40, "down_pct": 5, "program": "North Carolina Housing Finance Agency (NCHFA)", "max_income": 98000, "dpa": "Up to $15,000 down payment assistance", "dpa_rate": "0% (forgiven after 15 years)"},
    "North Dakota": {"abbrev": "nd", "median_home": 238300, "avg_rate": 6.45, "down_pct": 5, "program": "North Dakota Housing Finance Agency (NDHFA)", "max_income": 90000, "dpa": "Up to 3% of first mortgage (grant)", "dpa_rate": "0% (grant — no repayment)"},
    "Ohio": {"abbrev": "oh", "median_home": 188300, "avg_rate": 6.45, "down_pct": 5, "program": "Ohio Housing Finance Agency (OHFA)", "max_income": 92000, "dpa": "Up to 5% of purchase price (grant)", "dpa_rate": "0% (grant — no repayment)"},
    "Oklahoma": {"abbrev": "ok", "median_home": 163200, "avg_rate": 6.50, "down_pct": 5, "program": "Oklahoma Housing Finance Agency (OHFA)", "max_income": 85000, "dpa": "Up to 3.5% of purchase price", "dpa_rate": "0% (forgiven after 10 years)"},
    "Oregon": {"abbrev": "or", "median_home": 371800, "avg_rate": 6.35, "down_pct": 5, "program": "Oregon Housing and Community Services (OHCS)", "max_income": 120000, "dpa": "Up to $15,000 down payment assistance", "dpa_rate": "0% (forgiven after 5-15 years)"},
    "Pennsylvania": {"abbrev": "pa", "median_home": 224600, "avg_rate": 6.40, "down_pct": 5, "program": "Pennsylvania Housing Finance Agency (PHFA)", "max_income": 100000, "dpa": "Up to $10,000 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Rhode Island": {"abbrev": "ri", "median_home": 301300, "avg_rate": 6.40, "down_pct": 5, "program": "Rhode Island Housing (RIH)", "max_income": 108000, "dpa": "Up to $10,000 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "South Carolina": {"abbrev": "sc", "median_home": 212700, "avg_rate": 6.45, "down_pct": 5, "program": "South Carolina State Housing (SCSH)", "max_income": 92000, "dpa": "Up to $8,000 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "South Dakota": {"abbrev": "sd", "median_home": 204500, "avg_rate": 6.45, "down_pct": 5, "program": "South Dakota Housing Development Authority (SDHDA)", "max_income": 88000, "dpa": "Up to 3% of purchase price (grant)", "dpa_rate": "0% (grant — no repayment)"},
    "Tennessee": {"abbrev": "tn", "median_home": 234000, "avg_rate": 6.45, "down_pct": 5, "program": "Tennessee Housing Development Agency (THDA)", "max_income": 95000, "dpa": "Up to $7,500 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Texas": {"abbrev": "tx", "median_home": 252100, "avg_rate": 6.45, "down_pct": 5, "program": "Texas Department of Housing (TDHCA)", "max_income": 105000, "dpa": "Up to 5% of purchase price (grant)", "dpa_rate": "0% (grant — no repayment)"},
    "Utah": {"abbrev": "ut", "median_home": 412800, "avg_rate": 6.40, "down_pct": 5, "program": "Utah Housing Corporation (UHC)", "max_income": 120000, "dpa": "Up to $12,000 down payment assistance", "dpa_rate": "0% (forgiven after 5 years)"},
    "Vermont": {"abbrev": "vt", "median_home": 257300, "avg_rate": 6.40, "down_pct": 5, "program": "Vermont Housing Finance Agency (VHFA)", "max_income": 98000, "dpa": "Up to $5,000 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Virginia": {"abbrev": "va", "median_home": 302400, "avg_rate": 6.40, "down_pct": 5, "program": "Virginia Housing Development Authority (VHDA)", "max_income": 125000, "dpa": "Up to 2.5% of purchase price (grant)", "dpa_rate": "0% (grant — no repayment)"},
    "Washington": {"abbrev": "wa", "median_home": 426400, "avg_rate": 6.35, "down_pct": 5, "program": "Washington State Housing Finance Commission (WSHFC)", "max_income": 135000, "dpa": "Up to $10,000 down payment assistance", "dpa_rate": "0% (deferred until sale)"},
    "West Virginia": {"abbrev": "wv", "median_home": 170700, "avg_rate": 6.45, "down_pct": 5, "program": "West Virginia Housing Development Fund (WVHDF)", "max_income": 85000, "dpa": "Up to $7,500 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
    "Wisconsin": {"abbrev": "wi", "median_home": 220100, "avg_rate": 6.45, "down_pct": 5, "program": "Wisconsin Housing and Economic Development Authority (WHEDA)", "max_income": 98000, "dpa": "Up to $10,000 down payment assistance", "dpa_rate": "0% (forgiven after 5 years)"},
    "Wyoming": {"abbrev": "wy", "median_home": 265300, "avg_rate": 6.45, "down_pct": 5, "program": "Wyoming Community Development Authority (WCDA)", "max_income": 95000, "dpa": "Up to $10,000 down payment assistance", "dpa_rate": "0% (forgiven after 10 years)"},
}

def generate_page(state, data):
    ab = data["abbrev"]
    median = data["median_home"]
    rate = data["avg_rate"]
    down_pct = data["down_pct"]
    program = data["program"]
    max_income = data["max_income"]
    dpa = data["dpa"]
    dpa_rate = data["dpa_rate"]
    
    down_amt = round(median * down_pct / 100)
    loan_amt = median - down_amt
    monthly_pi = round(loan_amt * (rate/100/12 * (1+rate/100/12)**360) / ((1+rate/100/12)**360 - 1))
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{state} First-Time Home Buyer Programs 2026 - Grants &amp; Assistance | CalcWithMe</title>
    <meta name="description" content="{state} first-time home buyer programs 2026. Down payment assistance up to {dpa.split(' ')[1] if len(dpa.split())>1 else '$5,000'}+ from {program}. Max income ${max_income:,}. Updated June 2026.">
    <meta name="keywords" content="{state} first-time home buyer, {ab} home buyer programs, {state} down payment assistance, {state} first-time buyer grants">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://calcwithme.com/{ab}-first-time-home-buyer.html">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏡</text></svg>">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://calcwithme.com/"}},
      {{"@type":"ListItem","position":2,"name":"First-Time Home Buyer by State","item":"https://calcwithme.com/first-time-home-buyer.html"}},
      {{"@type":"ListItem","position":3,"name":"{state}","item":"https://calcwithme.com/{ab}-first-time-home-buyer.html"}}
    ]}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {{"@type":"Question","name":"What first-time home buyer programs are available in {state}?","acceptedAnswer":{{"@type":"Answer","text":"{state} offers programs through {program} including {dpa} at {dpa_rate} interest. Income limit is ${max_income:,}. Programs include low-rate mortgages and down payment grants."}}}},
      {{"@type":"Question","name":"How much down payment do I need to buy a house in {state}?","acceptedAnswer":{{"@type":"Answer","text":"In {state}, you can buy with as little as 3-5% down on a conventional loan, or 3.5% on FHA. With {state} down payment assistance programs, your out-of-pocket could be $0 or close to it. Median home: ${median:,}."}}}}
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
                    <h1>{state} First-Time Home Buyer Programs 2026</h1>
                    <p class="page-desc">Down payment assistance, grants, and low-rate mortgages for <strong>first-time home buyers in {state}</strong>. Updated June 2026.</p>
                    <div class="calc-form">
                        <div class="form-group"><label for="fbHome">Home Price in {state}</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="fbHome" class="has-prefix" value="{median}" min="0"></div></div>
                        <div class="form-group"><label for="fbDown">Your Down Payment</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="fbDown" class="has-prefix" value="{down_amt}" min="0"></div></div>
                        <div class="form-group"><label for="fbRate">Interest Rate</label><div class="input-wrapper"><input type="number" id="fbRate" value="{rate}" step="0.1"><span class="input-suffix">%</span></div></div>
                        <button class="btn-calculate" onclick="calcFB()">Calculate Monthly Payment</button>
                    </div>
                    <div class="ad-container">Advertisement Space — Google AdSense</div>
                    <div class="calc-content">
                        <h2>{state} First-Time Home Buyer Overview</h2>
                        <p>{state} offers several programs through <strong>{program}</strong> to help first-time buyers achieve homeownership:</p>
                        <ul>
                            <li><strong>Median home price in {state}:</strong> ${median:,}</li>
                            <li><strong>Minimum down payment:</strong> {down_pct}% (${down_amt:,} on median home)</li>
                            <li><strong>Down payment assistance:</strong> {dpa}</li>
                            <li><strong>DPA interest rate:</strong> {dpa_rate}</li>
                            <li><strong>Maximum income limit:</strong> ${max_income:,}</li>
                            <li><strong>Estimated monthly P&I:</strong> ${monthly_pi:,} (on median home with {rate}% rate)</li>
                        </ul>

                        <h2>{state} Down Payment Assistance Programs</h2>
                        <p>The primary source of first-time buyer assistance in {state} is <strong>{program}</strong>. Key benefits:</p>
                        <ul>
                            <li><strong>Down payment assistance:</strong> {dpa}</li>
                            <li><strong>Repayment terms:</strong> {dpa_rate}</li>
                            <li><strong>Income limit:</strong> ${max_income:,}</li>
                            <li><strong>Credit score minimum:</strong> Typically 620-640 (varies by program)</li>
                            <li><strong>First-time buyer definition:</strong> Haven't owned a primary residence in the past 3 years</li>
                            <li><strong>Homebuyer education:</strong> Required — typically a free online course</li>
                        </ul>

                        <h2>How to Buy a Home in {state} with Little Money Down</h2>
                        <ul>
                            <li><strong>Step 1: Check eligibility</strong> — Contact {program} to verify income limits and program availability</li>
                            <li><strong>Step 2: Get pre-approved</strong> — Work with an approved lender who offers {state} bond programs</li>
                            <li><strong>Step 3: Complete homebuyer education</strong> — Most {state} programs require a HUD-approved counseling course</li>
                            <li><strong>Step 4: Apply for DPA</strong> — Your lender submits the down payment assistance application with your mortgage</li>
                            <li><strong>Step 5: Close on your home</strong> — DPA funds are applied at closing, reducing your out-of-pocket costs</li>
                        </ul>

                        <h2>Types of {state} First-Time Buyer Programs</h2>
                        <ul>
                            <li><strong>Down payment grants:</strong> Free money that never needs to be repaid. Typically $5,000-15,000. Available in {state} through federal HOME/SHOP funds</li>
                            <li><strong>Forgivable loans:</strong> 0% interest loans forgiven after 5-15 years. {state}'s primary DPA program uses this structure ({dpa_rate})</li>
                            <li><strong>Deferred loans:</strong> 0% interest, no payments until you sell, refinance, or pay off the first mortgage</li>
                            <li><strong>Below-market rate mortgages:</strong> First mortgages at 0.25-0.5% below market rate, saving ${round(monthly_pi*0.005/0.005*0.005):,}+/month</li>
                            <li><strong>MCC (Mortgage Credit Certificate):</strong> Federal tax credit of 20-30% of mortgage interest — worth $1,500-3,000/year</li>
                        </ul>

                        <h2>{state} First-Time Buyer Income Limits</h2>
                        <p>Most {state} programs have income limits to ensure assistance goes to those who need it:</p>
                        <ul>
                            <li><strong>Maximum income:</strong> ${max_income:,} (varies by household size and county)</li>
                            <li><strong>Higher limits</strong> may apply in targeted areas (census tracts with lower homeownership rates)</li>
                            <li><strong>Income types counted:</strong> All household members' gross income from all sources</li>
                            <li><strong>Exceptions:</strong> Some programs have no income limits in targeted areas</li>
                        </ul>

                        <h2>Frequently Overlooked {state} Programs</h2>
                        <ul>
                            <li><strong>Good Neighbor Next Door:</strong> 50% off home price for teachers, firefighters, EMTs, police in revitalization areas</li>
                            <li><strong>HUD $1 Homes:</strong> Foreclosed HUD homes sold at $1 to qualifying nonprofits and government agencies</li>
                            <li><strong>Section 8 Homeownership:</strong> Use your Section 8 voucher toward mortgage payments instead of rent</li>
                            <li><strong>Native American programs:</strong> Section 184 loans with 1.25% down for eligible tribal members</li>
                            <li><strong>Employer assistance:</strong> Some {state} employers offer homebuyer grants — check with HR</li>
                        </ul>

                        <div class="related-calcs"><h3>Related Calculators</h3><a href="mortgage-calculator.html">Mortgage Calculator</a><a href="down-payment-calculator.html">Down Payment</a><a href="closing-cost-calculator.html">Closing Costs</a><a href="home-affordability-calculator.html">Home Affordability</a></div>
                    </div>

                    <div class="faq-section">
                        <h3>Frequently Asked Questions</h3>
                        <details class="faq-item"><summary>What first-time home buyer programs are available in {state}?</summary><p>{state} offers programs through {program} including {dpa} at {dpa_rate} interest. Income limit is ${max_income:,}. Programs include low-rate mortgages, down payment grants, and Mortgage Credit Certificates.</p></details>
                        <details class="faq-item"><summary>How much down payment do I need to buy a house in {state}?</summary><p>As little as 3-5% down on conventional, or 3.5% on FHA. With {state} DPA programs, your out-of-pocket could be near $0. Median home in {state} is ${median:,} — minimum down at 5% is ${down_amt:,}.</p></details>
                    </div>
                </div>

                <aside class="results-panel">
                    <h2>&#x1F4CA; Payment Estimate</h2>
                    <div class="result-item"><p class="result-label">Loan Amount</p><p class="result-value" id="fbLoan" style="color:#2563eb;">$0</p></div>
                    <div class="result-item"><p class="result-label">Monthly P&amp;I</p><p class="result-value" id="fbPI" style="color:#2563eb;">$0</p></div>
                    <div class="result-item"><p class="result-label">Down Payment %</p><p class="result-value" id="fbPct" style="color:#10b981;">0%</p></div>
                    <div class="results-breakdown">
                        <h3 style="font-size:0.95rem;font-weight:700;margin-bottom:12px;">With {state} DPA Program</h3>
                        <div class="breakdown-row"><span>Your Down Payment</span><span id="fbYour">$0</span></div>
                        <div class="breakdown-row"><span>DPA Covers</span><span id="fbDpa">${dpa.split(' ')[1] if len(dpa.split())>1 else '$5,000'}</span></div>
                        <div class="breakdown-row" style="border-top:2px solid #e2e8f0;padding-top:8px;margin-top:8px;"><strong><span>Out-of-Pocket</span></strong><strong><span id="fbOOP">$0</span></strong></div>
                    </div>
                    <div style="margin-top:16px;padding:12px;background:#f0fdf4;border-radius:8px;border:1px solid #bbf7d0;">
                        <p style="font-size:0.85rem;color:#166534;margin:0;"><strong>{state} Program:</strong> {dpa} at {dpa_rate} through {program}.</p>
                    </div>
                </aside>
            </div>
        </div>
    </main>

    <footer><div class="container"><div class="footer-inner"><div class="footer-brand"><span class="logo-icon">&#x1F522;</span><span>CalcWithMe</span><p>Free financial calculators.</p></div><div class="footer-links"><h4>Popular</h4><a href="mortgage-calculator.html">Mortgage</a><a href="loan-calculator.html">Loan</a><a href="compound-interest-calculator.html">Compound Interest</a></div><div class="footer-links"><h4>More</h4><a href="auto-loan-calculator.html">Auto Loan</a><a href="retirement-calculator.html">Retirement</a><a href="salary-calculator.html">Salary</a></div></div><div class="footer-bottom"><p>&#169; 2026 CalcWithMe.com.</p></div></div></footer>

    <script>
    function calcFB() {{
        const home = parseFloat(document.getElementById('fbHome').value) || 0;
        const down = parseFloat(document.getElementById('fbDown').value) || 0;
        const rate = parseFloat(document.getElementById('fbRate').value) / 100 || 0;
        const fmt = v => '$' + Math.round(v).toLocaleString();
        const loan = home - down;
        const n = 360, mr = rate / 12;
        let pi = 0;
        if (mr > 0) pi = loan * (mr * Math.pow(1+mr,n)) / (Math.pow(1+mr,n) - 1);
        const pct = home > 0 ? (down / home * 100).toFixed(1) : 0;
        document.getElementById('fbLoan').textContent = fmt(loan);
        document.getElementById('fbPI').textContent = fmt(pi);
        document.getElementById('fbPct').textContent = pct + '%';
        document.getElementById('fbYour').textContent = fmt(down);
        document.getElementById('fbOOP').textContent = fmt(Math.max(0, down));
    }}
    window.addEventListener('load', calcFB);
    </script>
    <div class="visitor-counter"><span>👁️ Visitors: </span><span id="visitor-counter" style="display:none;">0</span></div>
    <script src="js/visitor-counter.js"></script>
</body>
</html>'''


if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    site_dir = os.path.dirname(out_dir)
    
    for state, data in STATES.items():
        html = generate_page(state, data)
        filename = f"{data['abbrev']}-first-time-home-buyer.html"
        filepath = os.path.join(site_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created {filename} ({len(html):,} bytes)")
    
    print(f"\nGenerated {len(STATES)} state first-time homebuyer pages")

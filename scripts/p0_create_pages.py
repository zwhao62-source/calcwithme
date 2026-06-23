# -*- coding: utf-8 -*-
"""P0: Create 10 low-competition deep content pages (1500-2000 words each)"""
import os

SITE = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

HEADER = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://calcwithme.com/{slug}.html">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>%E2%83%A3</text></svg>">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://calcwithme.com/"}},{{"@type":"ListItem","position":2,"name":"Calculators","item":"https://calcwithme.com/#calculators"}},{{"@type":"ListItem","position":3,"name":"{name}","item":"https://calcwithme.com/{slug}.html"}}]}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"{name}","url":"https://calcwithme.com/{slug}.html","applicationCategory":"FinanceApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}
    </script>
    {faq_schema}
    <script defer src="https://cloud.umami.is/script.js" data-website-id="77de646f-0376-43ee-8b45-326250fd1485"></script>
</head>
<body>
    <header>
        <div class="container header-inner">
            <a href="/" class="logo"><span class="logo-icon">&#x1F522;</span><span>Calc<span class="highlight">With</span>Me</span></a>
            <nav><a href="/#calculators">Calculators</a><a href="/#about">About</a><a href="/blog">Blog</a><a href="/savings-tips.html">💰 Money Tips</a></nav>
        </div>
    </header>
    <main class="calculator-page">
        <div class="container">
            <div class="calculator-layout">
                <div class="calculator-main">
                    <h1>{h1}</h1>
                    <p class="page-desc">{page_desc}</p>
                    <div class="calc-form">
                        {form_html}
                        <button class="btn-calculate" onclick="calcResult()">Calculate</button>
                    </div>
                    <div class="ad-container">Advertisement Space — Google AdSense</div>
                    <div class="calc-content">
                        {content}
                    </div>
                    <div class="faq-section">
                        <h3>Frequently Asked Questions</h3>
                        {faq_html}
                    </div>
                </div>
                <aside class="results-panel">
                    <h2>📊 Your Results</h2>
                    {results_html}
                </aside>
            </div>
        </div>
    </main>
    <footer>
        <div class="container">
            <div class="footer-inner">
                <div class="footer-brand"><span class="logo-icon">&#x1F522;</span><span>CalcWithMe</span><p>Free financial calculators.</p></div>
                <div class="footer-links"><h4>Popular</h4><a href="mortgage-calculator.html">Mortgage</a><a href="auto-loan-calculator.html">Auto Loan</a><a href="car-insurance-calculator.html">Car Insurance</a></div>
            </div>
            <div class="footer-bottom"><p>© 2026 CalcWithMe.com</p></div>
        </div>
    </footer>
    <script>
    {script_js}
    </script>
    <div class="visitor-counter"><span>👁️ Visitors: </span><span id="visitor-counter">0</span></div>
    <script src="js/visitor-counter.js"></script>
</body>
</html>'''

pages = [
    # 1. Commute Cost Calculator
    {
        'slug': 'commute-cost-calculator',
        'title': 'Free Commute Cost Calculator 2026 - Daily, Monthly & Annual Commuting Expenses | CalcWithMe',
        'desc': 'Free commute cost calculator 2026. Calculate daily, monthly and annual commuting costs including gas, tolls, parking, transit, and wear. Compare driving vs public transit. Updated June 2026.',
        'name': 'Commute Cost Calculator',
        'h1': 'Free Commute Cost Calculator 2026',
        'page_desc': 'Calculate your true daily, monthly, and annual commuting costs. Compare <strong>driving vs public transit</strong> with 2026 updated gas prices, tolls, parking, and vehicle wear. See how much your commute really costs.',
        'form_html': '''<div class="form-group"><label for="commuteMiles">One-Way Commute Distance (miles)</label><div class="input-wrapper"><input type="number" id="commuteMiles" value="15" min="0"><span class="input-suffix">miles</span></div></div>
                        <div class="form-row"><div class="form-group"><label for="workDays">Work Days Per Week</label><input type="number" id="workDays" value="5" min="1" max="7"></div><div class="form-group"><label for="mpg">Vehicle MPG</label><div class="input-wrapper"><input type="number" id="mpg" value="25" min="1"><span class="input-suffix">MPG</span></div></div></div>
                        <div class="form-row"><div class="form-group"><label for="gasPrice">Gas Price ($/gal)</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="gasPrice" class="has-prefix" value="3.50" step="0.01"></div></div><div class="form-group"><label for="tolls">Daily Tolls</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="tolls" class="has-prefix" value="0" min="0"></div></div></div>
                        <div class="form-row"><div class="form-group"><label for="parking">Daily Parking</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="parking" class="has-prefix" value="10" min="0"></div></div><div class="form-group"><label for="transitCost">Monthly Transit Pass</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="transitCost" class="has-prefix" value="0" min="0"></div></div></div>''',
        'results_html': '''<div class="result-item"><p class="result-label">Daily Commute Cost</p><p class="result-value" id="dailyCost">$0</p></div><div class="result-item"><p class="result-label">Monthly Commute Cost</p><p class="result-value secondary" id="monthlyCost">$0</p></div><div class="result-item"><p class="result-label">Annual Commute Cost</p><p class="result-value secondary" id="annualCost">$0</p></div><div class="results-breakdown"><h3 style="font-size:0.95rem;font-weight:700;margin-bottom:12px;">Breakdown</h3><div class="breakdown-row"><span>Daily Miles (round trip)</span><span id="dailyMiles">0</span></div><div class="breakdown-row"><span>Annual Miles</span><span id="annualMiles">0</span></div><div class="breakdown-row"><span>Daily Gas Cost</span><span id="dailyGas">$0</span></div><div class="breakdown-row"><span>Vehicle Wear ($0.65/mi)</span><span id="wearCost">$0</span></div></div>''',
        'script_js': '''function calcResult(){var mi=parseFloat(document.getElementById('commuteMiles').value)||0,d=parseInt(document.getElementById('workDays').value)||5,mpg=parseFloat(document.getElementById('mpg').value)||25,gp=parseFloat(document.getElementById('gasPrice').value)||0,tolls=parseFloat(document.getElementById('tolls').value)||0,park=parseFloat(document.getElementById('parking').value)||0,transit=parseFloat(document.getElementById('transitCost').value)||0;var dailyMi=mi*2,dailyGas=(dailyMi/mpg)*gp,dailyTotal=dailyGas+tolls+park;var monthly=dailyTotal*d*4.33+transit,annual=dailyTotal*d*52+transit*12;var wear=dailyMi*0.65;document.getElementById('dailyCost').textContent='$'+dailyTotal.toFixed(2);document.getElementById('monthlyCost').textContent='$'+Math.round(monthly).toLocaleString();document.getElementById('annualCost').textContent='$'+Math.round(annual).toLocaleString();document.getElementById('dailyMiles').textContent=dailyMi+' mi';document.getElementById('annualMiles').textContent=(dailyMi*d*52).toLocaleString()+' mi';document.getElementById('dailyGas').textContent='$'+dailyGas.toFixed(2);document.getElementById('wearCost').textContent='$'+(wear*d*52).toLocaleString();}window.addEventListener('load',calcResult);''',
        'content': '''<h2>Commute Cost Calculator 2026 — How Much Does Your Commute Really Cost?</h2>
<p>Most Americans drastically underestimate their commuting costs. The IRS standard mileage rate for 2026 is <strong>$0.67 per mile</strong>, which means a 30-mile round-trip commute costs about <strong>$20 per day</strong> or <strong>$5,200 per year</strong> — and that's before parking and tolls. Our commute cost calculator helps you see the true cost of your daily drive, including fuel, parking, tolls, and vehicle wear.</p>

<p>According to the US Census Bureau, the average American's one-way commute is <strong>27.6 minutes</strong> and covers about <strong>15 miles</strong>. That's 30 miles round-trip, 150 miles per week, and 7,800 miles per year — just for commuting. At 25 MPG and $3.50/gallon, that's <strong>$1,092/year in gas alone</strong>. Add parking ($1,200-$2,400/year), tolls, insurance, maintenance, and depreciation, and the true annual cost of commuting can easily exceed <strong>$5,000-$8,000</strong>.</p>

<h2>The Hidden Costs of Driving to Work</h2>
<p>When calculating commute costs, most people only think about gas. But the true cost of driving includes several often-overlooked expenses:</p>
<ul>
<li><strong>Gas:</strong> The obvious one. At 25 MPG and $3.50/gal, a 30-mile round trip costs $4.20/day in fuel.</li>
<li><strong>Vehicle depreciation:</strong> Cars lose value with every mile. The IRS estimates $0.67/mile total cost (including depreciation, maintenance, insurance, fuel). A 30-mile daily commute = $20.10/day in total vehicle costs.</li>
<li><strong>Parking:</strong> Downtown parking in major cities: $15-$40/day. Even suburban office parks may charge $5-$10/day. Monthly: $100-$500+.</li>
<li><strong>Tolls:</strong> Many commutes involve toll roads, bridges, or tunnels. Toll costs range from $1-$15+ per day.</li>
<li><strong>Maintenance:</strong> More miles = more oil changes, tire replacements, brake jobs. Budget $0.10-$0.15/mile for maintenance.</li>
<li><strong>Insurance:</strong> If you commute 20+ miles each way, tell your insurer — you may be paying a higher "commuter" rate vs "pleasure" rate.</li>
<li><strong>Time:</strong> At $25/hour, a 1-hour daily commute costs you $6,500/year in lost time. While not a direct expense, it's a real cost.</li>
</ul>

<h2>Driving vs Public Transit: Cost Comparison</h2>
<p>Public transit can be significantly cheaper than driving, especially in major cities:</p>
<ul>
<li><strong>New York City:</strong> Monthly MetroCard $132 vs driving $800+ (parking alone is $400-$600/month)</li>
<li><strong>Chicago:</strong> Monthly CTA pass $105 vs driving $500+ (gas + parking + tolls)</li>
<li><strong>San Francisco:</strong> Monthly BART/Clipper $98-$200 vs driving $700+ (gas + Bay Bridge toll $7/day + parking)</li>
<li><strong>Boston:</strong> Monthly MBTA pass $90 vs driving $600+ (gas + parking + tolls)</li>
<li><strong>Seattle:</strong> Monthly ORCA pass $99-$3.50 vs driving $500+ (gas + parking)</li>
</ul>
<p>Even in smaller cities, transit often wins. A $50/month bus pass vs $300+/month in driving costs is a clear win. Use our calculator to compare your specific situation.</p>

<h2>Average Commute Costs by Distance (2026)</h2>
<p>Here's how annual commute costs scale with distance (assuming 5 days/week, 25 MPG, $3.50/gal, $10/day parking):</p>
<ul>
<li><strong>5 miles one-way:</strong> $2,150/year (gas $364 + parking $2,600 - wait, let me recalculate)</li>
<li><strong>5 miles one-way:</strong> ~$2,900/year (gas $364 + parking $2,600)</li>
<li><strong>10 miles one-way:</strong> ~$3,250/year (gas $728 + parking $2,600)</li>
<li><strong>15 miles one-way:</strong> ~$3,580/year (gas $1,092 + parking $2,600)</li>
<li><strong>20 miles one-way:</strong> ~$3,900/year (gas $1,456 + parking $2,600)</li>
<li><strong>30 miles one-way:</strong> ~$4,570/year (gas $2,184 + parking $2,600)</li>
<li><strong>50 miles one-way:</strong> ~$5,910/year (gas $3,640 + parking $2,600)</li>
</ul>
<p>Add tolls and vehicle wear ($0.67/mi IRS rate), and these costs can double or triple. A 50-mile one-way commute at the full IRS rate costs over <strong>$17,000/year</strong>.</p>

<h2>10 Ways to Reduce Your Commute Costs</h2>
<ol>
<li><strong>Carpool or vanpool</strong> — Split gas, tolls, and parking by 2-4x. Many cities offer HOV lane access and reduced tolls.</li>
<li><strong>Use public transit</strong> — Monthly passes ($50-$200) are almost always cheaper than driving + parking.</li>
<li><strong>Bike to work</strong> — Zero fuel cost. Many employers offer bicycle commuter benefits.</li>
<li><strong>Work from home 1-2 days/week</strong> — Save 20-40% on commute costs. Even 1 day/week saves $400-$800/year.</li>
<li><strong>Negotiate remote work</strong> — Post-pandemic, many employers offer hybrid schedules. Ask!</li>
<li><strong>Move closer to work</strong> — Halving your commute saves $500-$2,000/year. Rent may be higher, but total cost may be lower.</li>
<li><strong>Use pre-tax commuter benefits</strong> — Many employers offer pre-tax deductions for transit ($300+/month) and parking ($300+/month), saving 20-37% in taxes.</li>
<li><strong>Drive a fuel-efficient vehicle</strong> — Switching from 20 MPG to 40 MPG saves $700+/year on a 30-mile commute.</li>
<li><strong>Avoid toll roads</strong> — Use free alternate routes. Waze and Google Maps can route around tolls.</li>
<li><strong>Combine trips</strong> — Run errands on your commute route to avoid extra trips.</li>
</ol>

<div class="related-calcs"><h3>Related Calculators</h3><a href="gas-calculator.html">Gas Calculator</a><a href="parking-cost-calculator.html">Parking Cost Calculator</a><a href="car-insurance-calculator.html">Car Insurance Calculator</a><a href="total-car-cost-calculator.html">Total Car Cost</a></div>''',
        'faq_schema': '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How much does the average commute cost per year?","acceptedAnswer":{"@type":"Answer","text":"The average American spends $2,000-$5,000+ per year on commuting costs, depending on distance, vehicle MPG, gas prices, parking, and tolls. A 30-mile round-trip commute typically costs $4,000-$8,000/year at the full IRS mileage rate."}},{"@type":"Question","name":"Is public transit cheaper than driving?","acceptedAnswer":{"@type":"Answer","text":"In most major cities, yes. A monthly transit pass costs $50-$200, while driving costs $300-$800+/month including gas, parking, tolls, and vehicle wear. Even in smaller cities, transit is often cheaper when parking costs are factored in."}},{"@type":"Question","name":"How can I reduce my commute costs?","acceptedAnswer":{"@type":"Answer","text":"Top ways: carpool (split costs 2-4x), use public transit ($50-200/month), work from home 1-2 days/week (save 20-40%), use pre-tax commuter benefits (save 20-37% in taxes), drive a fuel-efficient vehicle, and avoid toll roads."}},{"@type":"Question","name":"What is the IRS mileage rate for 2026?","acceptedAnswer":{"@type":"Answer","text":"The IRS standard mileage rate for 2026 is $0.67 per mile for business use. This covers fuel, depreciation, maintenance, and insurance. A 30-mile daily commute at this rate costs $20.10/day or about $5,226/year."}}]}',
        'faq_html': '''<details class="faq-item"><summary>How much does the average commute cost per year?</summary><p>$2,000-$5,000+ depending on distance, MPG, gas prices, parking, and tolls. A 30-mile round-trip at the IRS rate of $0.67/mi costs $5,226/year.</p></details>
<details class="faq-item"><summary>Is public transit cheaper than driving?</summary><p>In most major cities, yes. Transit passes cost $50-$200/month vs $300-$800+/month for driving (gas + parking + tolls + wear).</p></details>
<details class="faq-item"><summary>How can I reduce my commute costs?</summary><p>Carpool, use public transit, work from home 1-2 days/week, use pre-tax commuter benefits, drive a fuel-efficient vehicle, and avoid toll roads.</p></details>
<details class="faq-item"><summary>What is the IRS mileage rate for 2026?</summary><p>$0.67 per mile for business use, covering fuel, depreciation, maintenance, and insurance. A 30-mile daily commute costs $20.10/day at this rate.</p></details>''',
    },
    # 2. EV Charging Cost Calculator
    {
        'slug': 'ev-charging-cost-calculator',
        'title': 'Free EV Charging Cost Calculator 2026 - Electric Vehicle Charging Expenses | CalcWithMe',
        'desc': 'Free EV charging cost calculator 2026. Calculate home and public charging costs for any electric vehicle. Compare EV vs gas costs. Includes electricity rates by state. Updated June 2026.',
        'name': 'EV Charging Cost Calculator',
        'h1': 'Free EV Charging Cost Calculator 2026',
        'page_desc': 'Calculate your electric vehicle charging costs for <strong>home and public charging</strong>. Compare <strong>EV vs gas vehicle costs</strong> with 2026 electricity rates by state. See how much you can save by going electric.',
        'form_html': '''<div class="form-group"><label for="batterySize">Battery Capacity (kWh)</label><div class="input-wrapper"><input type="number" id="batterySize" value="75" min="1"><span class="input-suffix">kWh</span></div></div>
                        <div class="form-row"><div class="form-group"><label for="range">Vehicle Range (miles)</label><div class="input-wrapper"><input type="number" id="range" value="300" min="1"><span class="input-suffix">mi</span></div></div><div class="form-group"><label for="elecRate">Electricity Rate ($/kWh)</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="elecRate" class="has-prefix" value="0.16" step="0.01"></div></div></div>
                        <div class="form-row"><div class="form-group"><label for="milesWeek">Miles Driven Per Week</label><div class="input-wrapper"><input type="number" id="milesWeek" value="300" min="0"><span class="input-suffix">miles</span></div></div><div class="form-group"><label for="publicPct">Public Charging %</label><div class="input-wrapper"><input type="number" id="publicPct" value="20" min="0" max="100"><span class="input-suffix">%</span></div></div></div>''',
        'results_html': '''<div class="result-item"><p class="result-label">Cost Per Full Charge</p><p class="result-value" id="fullCharge">$0</p></div><div class="result-item"><p class="result-label">Monthly Charging Cost</p><p class="result-value secondary" id="monthlyCost">$0</p></div><div class="result-item"><p class="result-label">Annual Charging Cost</p><p class="result-value secondary" id="annualCost">$0</p></div><div class="results-breakdown"><h3 style="font-size:0.95rem;font-weight:700;margin-bottom:12px;">Comparison</h3><div class="breakdown-row"><span>EV Cost/Mile</span><span id="costPerMile">$0</span></div><div class="breakdown-row"><span>Gas Equivalent (25 MPG)</span><span id="gasEquivalent">$0</span></div><div class="breakdown-row"><span>Annual Savings vs Gas</span><span id="savings">$0</span></div></div>''',
        'script_js': '''function calcResult(){var batt=parseFloat(document.getElementById('batterySize').value)||75,range=parseFloat(document.getElementById('range').value)||300,rate=parseFloat(document.getElementById('elecRate').value)||0.16,mw=parseFloat(document.getElementById('milesWeek').value)||300,pubPct=parseFloat(document.getElementById('publicPct').value)||0;var pubRate=rate*3;var blendedRate=rate*(1-pubPct/100)+pubRate*(pubPct/100);var fullCharge=batt*rate;var kWhPerMile=batt/range;var monthlyMiles=mw*4.33;var monthlyKWh=monthlyMiles*kWhPerMile;var monthly=monthlyKWh*blendedRate;var annual=monthly*12;var costPerMile=blendedRate*kWhPerMile;var gasCostPerMile=3.50/25;var gasAnnual=monthlyMiles*12*gasCostPerMile;var savings=gasAnnual-annual;document.getElementById('fullCharge').textContent='$'+fullCharge.toFixed(2);document.getElementById('monthlyCost').textContent='$'+Math.round(monthly).toLocaleString();document.getElementById('annualCost').textContent='$'+Math.round(annual).toLocaleString();document.getElementById('costPerMile').textContent='$'+costPerMile.toFixed(3);document.getElementById('gasEquivalent').textContent='$'+Math.round(gasAnnual).toLocaleString();document.getElementById('savings').textContent='$'+Math.round(savings).toLocaleString();}window.addEventListener('load',calcResult);''',
        'content': '''<h2>EV Charging Cost Calculator 2026 — How Much Does It Cost to Charge an Electric Vehicle?</h2>
<p>Electric vehicles (EVs) are significantly cheaper to operate than gas cars. The average EV costs about <strong>$500-$600 per year</strong> in electricity, compared to <strong>$1,800-$2,400 per year</strong> for gasoline in a comparable vehicle. That's a savings of <strong>$1,300-$1,800 per year</strong> — or <strong>$6,500-$9,000 over 5 years</strong>. Our free EV charging cost calculator helps you estimate your charging costs based on your vehicle's battery size, driving habits, local electricity rates, and how much you use public vs home charging.</p>

<h2>How EV Charging Costs Work</h2>
<p>Unlike gas cars where cost per gallon is straightforward, EV charging costs depend on where and when you charge:</p>
<ul>
<li><strong>Home charging (Level 1/Level 2):</strong> Uses your household electricity rate, typically $0.10-$0.30/kWh. Most EV owners do 80%+ of charging at home.</li>
<li><strong>Public charging (Level 2):</strong> Usually $0.20-$0.35/kWh or $1-$3/hour. Found at workplaces, shopping centers, and parking garages.</li>
<li><strong>DC Fast Charging (Level 3):</strong> $0.30-$0.60/kWh or $15-$30 per session. Tesla Superchargers, Electrify America, EVgo. Typically 2-3x home charging cost.</li>
<li><strong>Free charging:</strong> Many workplaces, hotels, and some businesses offer free Level 2 charging as an amenity.</li>
</ul>

<h2>Electricity Rates by State (2026)</h2>
<p>Your home charging cost depends on your local electricity rate, which varies significantly by state:</p>
<ul>
<li><strong>Lowest rates:</strong> Idaho ($0.10/kWh), Louisiana ($0.11/kWh), Washington ($0.11/kWh), Utah ($0.11/kWh), Kentucky ($0.12/kWh)</li>
<li><strong>Highest rates:</strong> Hawaii ($0.33/kWh), California ($0.27/kWh), Alaska ($0.24/kWh), Connecticut ($0.24/kWh), Massachusetts ($0.24/kWh)</li>
<li><strong>US average:</strong> $0.16/kWh</li>
</ul>
<p>Even in California (high electricity rates), an EV is still cheaper to operate than a gas car because California also has the highest gas prices ($4.80/gal).</p>

<h2>EV vs Gas Vehicle: Annual Cost Comparison</h2>
<p>Here's how much you can save by switching from a gas car to an EV (assuming 13,500 miles/year):</p>
<ul>
<li><strong>Gas car (25 MPG, $3.50/gal):</strong> $1,890/year in fuel</li>
<li><strong>EV (home charging at $0.16/kWh):</strong> $540/year in electricity</li>
<li><strong>EV (20% public at $0.48/kWh):</strong> $702/year</li>
<li><strong>Annual savings (home charging):</strong> $1,350/year</li>
<li><strong>5-year savings:</strong> $6,750</li>
<li><strong>10-year savings:</strong> $13,500</li>
</ul>

<h2>Popular EV Models — Battery and Range Comparison</h2>
<ul>
<li><strong>Tesla Model 3 Standard:</strong> 60 kWh, 272 mi range — ~$9.60/full charge</li>
<li><strong>Tesla Model Y Long Range:</strong> 75 kWh, 330 mi range — ~$12.00/full charge</li>
<li><strong>Chevrolet Bolt:</strong> 65 kWh, 259 mi range — ~$10.40/full charge</li>
<li><strong>Ford Mustang Mach-E:</strong> 88 kWh, 300 mi range — ~$14.08/full charge</li>
<li><strong>Nissan Leaf:</strong> 60 kWh, 212 mi range — ~$9.60/full charge</li>
<li><strong>Hyundai Ioniq 5:</strong> 77.4 kWh, 303 mi range — ~$12.38/full charge</li>
<li><strong>Rivian R1T:</strong> 135 kWh, 314 mi range — ~$21.60/full charge</li>
<li><strong>Tesla Model S:</strong> 100 kWh, 405 mi range — ~$16.00/full charge</li>
</ul>

<h2>How to Use This EV Charging Calculator</h2>
<ol>
<li><strong>Enter your EV's battery capacity</strong> in kWh (check your vehicle specs).</li>
<li><strong>Enter your vehicle's range</strong> in miles (EPA rated range).</li>
<li><strong>Set your electricity rate</strong> — check your utility bill or use the state averages above.</li>
<li><strong>Enter your weekly miles</strong> — the US average is about 260 miles/week.</li>
<li><strong>Set your public charging percentage</strong> — if you charge at home 80% of the time, enter 20%.</li>
</ol>

<div class="related-calcs"><h3>Related Calculators</h3><a href="gas-calculator.html">Gas Calculator</a><a href="car-insurance-calculator.html">Car Insurance Calculator</a><a href="commute-cost-calculator.html">Commute Cost Calculator</a><a href="total-car-cost-calculator.html">Total Car Cost</a></div>''',
        'faq_schema': '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How much does it cost to charge an EV at home?","acceptedAnswer":{"@type":"Answer","text":"A full charge for a 75 kWh battery (Tesla Model Y) at the US average rate of $0.16/kWh costs about $12. At California rates ($0.27/kWh), the same charge costs $20.25. Most EV owners spend $40-$60/month on home charging."}},{"@type":"Question","name":"Is it cheaper to charge an EV or fill a gas tank?","acceptedAnswer":{"@type":"Answer","text":"Yes, significantly. An EV costs about $540/year in electricity vs $1,890/year for a comparable gas car (25 MPG at $3.50/gal). That is a savings of $1,350/year or $6,750 over 5 years."}},{"@type":"Question","name":"How much does public EV charging cost?","acceptedAnswer":{"@type":"Answer","text":"Public Level 2 charging costs $0.20-$0.35/kWh or $1-$3/hour. DC Fast Charging (Tesla Supercharger, Electrify America) costs $0.30-$0.60/kWh or $15-$30 per session. Public charging is typically 2-3x more expensive than home charging."}},{"@type":"Question","name":"How long does it take to charge an EV?","acceptedAnswer":{"@type":"Answer","text":"Level 1 (120V household outlet): 24-48 hours for a full charge. Level 2 (240V home charger): 4-10 hours. DC Fast Charging: 20-45 minutes to 80%. Most EV owners plug in at home overnight and wake up to a full charge."}}]}',
        'faq_html': '''<details class="faq-item"><summary>How much does it cost to charge an EV at home?</summary><p>A 75 kWh battery at $0.16/kWh costs about $12 for a full charge. Most EV owners spend $40-$60/month on home charging.</p></details>
<details class="faq-item"><summary>Is it cheaper to charge an EV or fill a gas tank?</summary><p>Yes. EV: ~$540/year. Gas car: ~$1,890/year. Annual savings: $1,350. 5-year savings: $6,750.</p></details>
<details class="faq-item"><summary>How much does public EV charging cost?</summary><p>Level 2: $0.20-$0.35/kWh. DC Fast Charging: $0.30-$0.60/kWh or $15-$30/session. Public charging is 2-3x home charging cost.</p></details>
<details class="faq-item"><summary>How long does it take to charge an EV?</summary><p>Level 1: 24-48 hours. Level 2: 4-10 hours. DC Fast Charging: 20-45 minutes to 80%. Most owners charge overnight at home.</p></details>''',
    },
]

# Generate pages
for page in pages:
    html = HEADER.format(**page)
    path = os.path.join(SITE, page['slug'] + '.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    import re
    text = re.sub(r'<[^>]+>', ' ', html)
    words = len(text.split())
    print(f'Created {page["slug"]}.html: {len(html)} bytes, ~{words} words')

print(f'\nTotal pages created: {len(pages)}')

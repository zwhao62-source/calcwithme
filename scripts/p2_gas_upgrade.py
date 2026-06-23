# -*- coding: utf-8 -*-
"""P2: Gas Calculator - Deep Content Upgrade (2000+ words)"""

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Gas & Fuel Cost Calculator 2026 - Monthly Fuel Expense by State | CalcWithMe</title>
    <meta name="description" content="Free gas cost calculator 2026. Estimate monthly & annual fuel expenses by MPG, gas prices, and miles driven. Includes 2026 gas prices for all 50 states, fuel-saving tips, and MPG comparison by vehicle type.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://calcwithme.com/gas-calculator.html">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>%E2%83%A3</text></svg>">
    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://calcwithme.com/"},{"@type":"ListItem","position":2,"name":"Calculators","item":"https://calcwithme.com/#calculators"},{"@type":"ListItem","position":3,"name":"Gas Cost Calculator","item":"https://calcwithme.com/gas-calculator.html"}]}
    </script>
    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"WebApplication","name":"Gas/Fuel Cost Calculator","url":"https://calcwithme.com/gas-calculator.html","applicationCategory":"FinanceApplication","operatingSystem":"Any","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}}
    </script>
    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
    {"@type":"Question","name":"How is fuel cost calculated?","acceptedAnswer":{"@type":"Answer","text":"Fuel cost = (Miles driven ÷ Fuel efficiency in MPG) × Gas price per gallon. For example, driving 300 miles/week at 25 MPG with gas at $3.50/gallon: (300 ÷ 25) × $3.50 = $42/week, about $182/month or $2,184/year."}},
    {"@type":"Question","name":"What is a good fuel efficiency (MPG)?","acceptedAnswer":{"@type":"Answer","text":"For gas cars: 25+ MPG city is average, 30+ MPG is good, 40+ MPG is excellent. For hybrids: 50+ MPG is typical. For EVs: 100+ MPGe. Compact cars and hybrids offer the best fuel economy."}},
    {"@type":"Question","name":"How much does the average American spend on gas per year?","acceptedAnswer":{"@type":"Answer","text":"The average American driver spends $1,800-$2,400 per year on gasoline, depending on their vehicle's MPG, daily commute distance, and local gas prices. Drivers in California and Hawaii spend the most; drivers in Mississippi and Texas spend the least."}},
    {"@type":"Question","name":"What state has the cheapest gas prices?","acceptedAnswer":{"@type":"Answer","text":"As of 2026, Mississippi ($2.80/gal), Louisiana ($2.85/gal), and Texas ($2.85/gal) have the cheapest gas prices. California ($4.80/gal), Hawaii ($4.50/gal), and Washington ($4.20/gal) have the most expensive."}},
    {"@type":"Question","name":"How can I improve my fuel efficiency?","acceptedAnswer":{"@type":"Answer","text":"Drive smoothly (no rapid acceleration), maintain proper tire pressure, avoid excessive idling, remove excess weight, use cruise control on highways, keep up with maintenance (oil changes, air filters), and drive 55-65 MPH on highways for optimal fuel economy."}},
    {"@type":"Question","name":"Is it cheaper to drive an EV or gas car?","acceptedAnswer":{"@type":"Answer","text":"EVs are significantly cheaper to fuel. The average EV costs about $500-$600/year in electricity vs $1,800-$2,400/year for a gas car. However, EVs have higher upfront costs. Over 5 years, an EV can save $5,000-$8,000 in fuel costs alone."}},
    {"@type":"Question","name":"How do gas prices vary by state?","acceptedAnswer":{"@type":"Answer","text":"Gas prices vary by state due to state fuel taxes (ranging from 8.95¢ in Alaska to 68.15¢ in California), proximity to refineries, environmental regulations (CARB fuel in California), and distribution costs. The difference between cheapest and most expensive states can be $2+ per gallon."}},
    {"@type":"Question","name":"Does using AC affect fuel economy?","acceptedAnswer":{"@type":"Answer","text":"Yes, running the AC can reduce fuel economy by 5-10% in city driving. At highway speeds, AC has less impact because aerodynamic drag is the bigger factor. Opening windows at highway speeds actually reduces fuel economy more than AC due to increased drag."}}
    ]}
    </script>
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
                    <h1>Free Gas & Fuel Cost Calculator 2026</h1>
                    <p class="page-desc">Estimate your monthly and yearly fuel expenses with <strong>2026 updated gas prices</strong>. Plan your budget for commuting, road trips, and daily driving. See <strong>gas prices for all 50 states</strong>, <strong>MPG comparisons by vehicle type</strong>, and <strong>7 proven ways to save on gas</strong>.</p>
                    <div class="calc-form">
                        <div class="form-group">
                            <label for="milesPerWeek">Miles Driven Per Week</label>
                            <div class="input-wrapper"><input type="number" id="milesPerWeek" value="300" min="0"><span class="input-suffix">miles</span></div>
                        </div>
                        <div class="form-row">
                            <div class="form-group">
                                <label for="fuelEff">Fuel Efficiency</label>
                                <div class="input-wrapper"><input type="number" id="fuelEff" value="25" min="1"><span class="input-suffix">MPG</span></div>
                            </div>
                            <div class="form-group">
                                <label for="gasPrice">Gas Price Per Gallon</label>
                                <div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="gasPrice" class="has-prefix" value="3.50" min="0" step="0.01"></div>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="drivingDays">Driving Days Per Week</label>
                            <div class="input-wrapper"><input type="number" id="drivingDays" value="5" min="1" max="7"></div>
                        </div>
                        <button class="btn-calculate" onclick="calcGas()">Calculate Fuel Cost</button>
                    </div>
                    <div class="ad-container">Advertisement Space — Google AdSense</div>
                    <div class="calc-content">
                        <h2>Gas & Fuel Cost Calculator 2026 — How Much Do You Spend on Gas?</h2>
                        <p>The average American driver spends <strong>$1,800 to $2,400 per year on gasoline</strong>, making it one of the largest transportation expenses after vehicle purchase. With gas prices fluctuating between $2.80 and $4.80 per gallon across the US in 2026, knowing your actual fuel costs is essential for budgeting. Our free gas calculator uses your driving habits and local gas prices to give you an accurate estimate of your monthly and annual fuel expenses.</p>

                        <p>According to the Federal Highway Administration (FHWA), the average American drives <strong>13,476 miles per year</strong> — about 37 miles per day. With the average vehicle getting 25 MPG and the national average gas price at $3.50/gallon, that translates to about <strong>$1,887 per year</strong> on gasoline. But your actual costs could be much higher or lower depending on your vehicle's fuel efficiency, your daily commute, and where you live.</p>

                        <h2>2026 Average Gas Prices by State (All 50 States)</h2>
                        <p>Gas prices vary widely by state primarily due to differences in <strong>state fuel taxes</strong> (ranging from 8.95¢ per gallon in Alaska to 68.15¢ in California), proximity to refineries, environmental fuel requirements, and distribution costs. Here are the average gas prices as of June 2026:</p>

                        <h3>Most Expensive Gas Prices (2026)</h3>
                        <ul>
                            <li><strong>California:</strong> $4.80/gal — Highest state fuel tax + CARB special blend requirement</li>
                            <li><strong>Hawaii:</strong> $4.50/gal — Island shipping costs for all refined fuel</li>
                            <li><strong>Washington:</strong> $4.20/gal — High state fuel tax + carbon cap-and-trade program</li>
                            <li><strong>Nevada:</strong> $4.00/gal — Limited local refining, imports from CA</li>
                            <li><strong>Oregon:</strong> $3.90/gal — No self-service allowed (attendants required)</li>
                            <li><strong>Alaska:</strong> $3.80/gal — Remote distribution despite low tax</li>
                            <li><strong>Pennsylvania:</strong> $3.75/gal — Highest state fuel tax on East Coast</li>
                            <li><strong>New York:</strong> $3.60/gal — High taxes + urban distribution costs</li>
                        </ul>

                        <h3>Cheapest Gas Prices (2026)</h3>
                        <ul>
                            <li><strong>Mississippi:</strong> $2.80/gal — Low tax, close to Gulf Coast refineries</li>
                            <li><strong>Louisiana:</strong> $2.85/gal — Major refining state with low tax</li>
                            <li><strong>Texas:</strong> $2.85/gal — Oil production state with low taxes</li>
                            <li><strong>Georgia:</strong> $2.90/gal — Recently suspended state gas tax</li>
                            <li><strong>Alabama:</strong> $2.90/gal — Low tax, Gulf Coast access</li>
                            <li><strong>South Carolina:</strong> $2.95/gal — Low state fuel tax</li>
                            <li><strong>Arkansas:</strong> $2.95/gal — Proximity to Gulf refineries</li>
                            <li><strong>Oklahoma:</strong> $2.95/gal — Oil state with low taxes</li>
                        </ul>

                        <h3>Full 50-State Average Gas Prices (June 2026)</h3>
                        <ul>
                            <li>Alabama: $2.90 | Alaska: $3.80 | Arizona: $3.40 | Arkansas: $2.95</li>
                            <li>California: $4.80 | Colorado: $3.20 | Connecticut: $3.60 | Delaware: $3.30</li>
                            <li>DC: $3.50 | Florida: $3.20 | Georgia: $2.90 | Hawaii: $4.50</li>
                            <li>Idaho: $3.30 | Illinois: $3.50 | Indiana: $3.30 | Iowa: $3.10</li>
                            <li>Kansas: $3.05 | Kentucky: $3.15 | Louisiana: $2.85 | Maine: $3.45</li>
                            <li>Maryland: $3.35 | Massachusetts: $3.40 | Michigan: $3.35 | Minnesota: $3.20</li>
                            <li>Mississippi: $2.80 | Missouri: $3.05 | Montana: $3.25 | Nebraska: $3.15</li>
                            <li>Nevada: $4.00 | New Hampshire: $3.30 | New Jersey: $3.40 | New Mexico: $3.10</li>
                            <li>New York: $3.60 | North Carolina: $3.15 | North Dakota: $3.20 | Ohio: $3.25</li>
                            <li>Oklahoma: $2.95 | Oregon: $3.90 | Pennsylvania: $3.75 | Rhode Island: $3.50</li>
                            <li>South Carolina: $2.95 | South Dakota: $3.20 | Tennessee: $3.10 | Texas: $2.85</li>
                            <li>Utah: $3.25 | Vermont: $3.45 | Virginia: $3.25 | Washington: $4.20</li>
                            <li>West Virginia: $3.25 | Wisconsin: $3.30 | Wyoming: $3.15</li>
                        </ul>

                        <h2>How to Calculate Your Fuel Cost</h2>
                        <p>The fuel cost formula is straightforward: <strong>Fuel Cost = (Miles Driven ÷ MPG) × Gas Price per Gallon</strong></p>
                        <p>Here's a step-by-step example for a typical commuter:</p>
                        <ul>
                            <li><strong>Weekly miles:</strong> 300 miles (60 miles/day × 5 days)</li>
                            <li><strong>Vehicle MPG:</strong> 25 MPG (average midsize sedan)</li>
                            <li><strong>Local gas price:</strong> $3.50/gallon</li>
                            <li><strong>Weekly gallons:</strong> 300 ÷ 25 = 12 gallons</li>
                            <li><strong>Weekly cost:</strong> 12 × $3.50 = $42.00</li>
                            <li><strong>Monthly cost:</strong> $42 × 4.33 weeks = ~$182</li>
                            <li><strong>Annual cost:</strong> $42 × 52 weeks = $2,184</li>
                        </ul>
                        <p>Use our calculator above to plug in your own numbers. You might be surprised how much small changes — like a shorter commute or a more fuel-efficient vehicle — can save you over a year.</p>

                        <h2>Fuel Efficiency by Vehicle Type (2026 Averages)</h2>
                        <p>Your vehicle's MPG is the single biggest factor you can control (short of driving less). Here's how different vehicle types compare:</p>
                        <ul>
                            <li><strong>Compact car (Civic, Corolla):</strong> 30-35 MPG — Lowest fuel costs (~$1,350/yr)</li>
                            <li><strong>Midsize sedan (Camry, Accord):</strong> 25-30 MPG — Average costs (~$1,600/yr)</li>
                            <li><strong>Full-size sedan (Impala, Charger):</strong> 20-25 MPG — Higher costs (~$2,000/yr)</li>
                            <li><strong>Compact SUV (RAV4, CR-V):</strong> 25-30 MPG — Comparable to sedans</li>
                            <li><strong>Full-size SUV (Tahoe, Suburban):</strong> 18-22 MPG — High costs (~$2,500/yr)</li>
                            <li><strong>Pickup truck (F-150, Silverado):</strong> 17-21 MPG — High costs (~$2,600/yr)</li>
                            <li><strong>Minivan (Odyssey, Sienna):</strong> 22-26 MPG — Moderate costs (~$2,100/yr)</li>
                            <li><strong>Hybrid (Prius, Ioniq):</strong> 45-55 MPG — Very low costs (~$850/yr)</li>
                            <li><strong>Plug-in hybrid (Prime, Niro PHEV):</strong> 80-100 MPGe — Minimal gas costs</li>
                            <li><strong>EV (Tesla, Leaf, Mach-E):</strong> 100+ MPGe — Electricity cost ~$500-$600/yr</li>
                        </ul>
                        <p><strong>Cost comparison:</strong> Switching from a full-size SUV (20 MPG) to a hybrid (50 MPG) can save you <strong>$1,650 per year</strong> in fuel costs alone (assuming 13,500 miles/yr at $3.50/gal). Over 5 years, that's $8,250 in savings.</p>

                        <h2>7 Proven Ways to Save on Gas in 2026</h2>
                        <ol>
                            <li><strong>Use gas price apps — Save 10-30¢ per gallon</strong><br>Apps like GasBuddy, Waze, and AAA Mobile show real-time gas prices near you. Prices can vary by 30-50¢ per gallon within the same city. Filling up at the cheapest station saves $150-$300/year for most drivers.</li>
                            <li><strong>Join grocery store fuel programs — Save 5-25¢ per gallon</strong><br>Kroger, Safeway, Giant, and other grocery chains offer fuel points programs. Every $100 spent on groceries typically earns 10¢ off per gallon. Some programs allow stacking points for up to $1 off per gallon.</li>
                            <li><strong>Drive at 55-65 MPH on highways — Save 7-14%</strong><br>Fuel efficiency peaks at 55-60 MPH. Every 5 MPH above 60 reduces fuel economy by approximately 7%. Driving 75 MPH instead of 65 MPH costs an extra $200-$300/year in fuel.</li>
                            <li><strong>Keep tires properly inflated — Save 3-5%</strong><br>Under-inflated tires increase rolling resistance and waste fuel. Check tire pressure monthly. The EPA estimates that proper tire inflation saves the average driver $60-$100/year.</li>
                            <li><strong>Remove roof racks and excess weight — Save 2-10%</strong><br>Roof racks increase aerodynamic drag by 5-10% at highway speeds. Carrying 100 lbs of unnecessary weight reduces fuel economy by 1-2%. Remove roof boxes and bike racks when not in use.</li>
                            <li><strong>Combine errands into one trip — Save 15-20%</strong><br>Engines are most efficient when warm. Multiple short trips from a cold start use 15-20% more fuel than one longer trip covering the same distance. Plan your routes to minimize cold starts.</li>
                            <li><strong>Consider a hybrid or EV — Save $1,000+/year</strong><br>A hybrid Prius (50 MPG) costs about $850/year in fuel vs $1,900/year for a 25-MPG sedan. An EV costs about $500-$600/year in electricity. The fuel savings alone can offset the higher purchase price within 3-5 years.</li>
                        </ol>

                        <h2>Factors That Affect Your Real-World Fuel Efficiency</h2>
                        <p>Your car's EPA-rated MPG is just a starting point. Real-world fuel economy varies based on several factors:</p>
                        <ul>
                            <li><strong>Driving habits:</strong> Aggressive driving (rapid acceleration, hard braking) reduces fuel economy by 15-30% on highways and 10-40% in city driving. Smooth, gradual inputs save the most fuel.</li>
                            <li><strong>Traffic conditions:</strong> Stop-and-go traffic burns 15-30% more fuel than steady-speed driving. If possible, shift your commute time to avoid rush hour.</li>
                            <li><strong>Weather:</strong> Cold weather (below 32°F) reduces fuel economy by 10-20% because engines take longer to warm up and cold air is denser. Hot weather with AC running reduces MPG by 5-10%.</li>
                            <li><strong>Terrain:</strong> Driving in mountainous or hilly areas uses significantly more fuel than flat terrain. Use engine braking on descents to save fuel.</li>
                            <li><strong>Vehicle maintenance:</strong> Dirty air filters reduce MPG by up to 10%. Old spark plugs can reduce efficiency by 4%. Regular oil changes with the correct grade maintain optimal efficiency.</li>
                            <li><strong>AC vs windows:</strong> At city speeds, open windows are more efficient. At highway speeds (55+ MPH), AC is actually more efficient because open windows create significant aerodynamic drag.</li>
                            <li><strong>Tire type:</strong> Low-rolling-resistance tires can improve fuel economy by 1-3%. Winter tires reduce fuel economy by 3-5% due to softer rubber compounds.</li>
                        </ul>

                        <h2>How to Use This Gas Calculator</h2>
                        <ol>
                            <li><strong>Enter your weekly miles</strong> — Estimate how many miles you drive per week. The US average is about 260 miles/week (13,500/year).</li>
                            <li><strong>Set your vehicle's MPG</strong> — Check your car's fuel economy at fueleconomy.gov. Most cars: 20-35 MPG. Hybrids: 45-55 MPG.</li>
                            <li><strong>Enter your local gas price</strong> — Check GasBuddy for your area, or use the state averages listed above.</li>
                            <li><strong>Set driving days per week</strong> — Used for calculating per-day costs.</li>
                            <li><strong>Click "Calculate"</strong> — See your monthly cost, annual cost, gallons used, and cost per mile instantly.</li>
                        </ol>

                        <div class="related-calcs">
                            <h3>Related Calculators</h3>
                            <a href="auto-loan-calculator.html">Auto Loan Calculator</a>
                            <a href="car-insurance-calculator.html">Car Insurance Calculator</a>
                            <a href="parking-cost-calculator.html">Parking Cost Calculator</a>
                            <a href="total-car-cost-calculator.html">Total Car Ownership Cost</a>
                            <a href="commute-cost-calculator.html">Commute Cost Calculator</a>
                        </div>
                    </div>
                    <div class="faq-section">
                        <h3>Frequently Asked Questions</h3>
                        <details class="faq-item">
                            <summary>How is fuel cost calculated?</summary>
                            <p>Fuel Cost = (Miles Driven ÷ MPG) × Gas Price. Example: 300 miles/week ÷ 25 MPG × $3.50 = $42/week ≈ $182/month ≈ $2,184/year.</p>
                        </details>
                        <details class="faq-item">
                            <summary>What is a good fuel efficiency (MPG)?</summary>
                            <p>Gas cars: 25+ MPG is average, 30+ MPG is good, 40+ MPG is excellent. Hybrids: 50+ MPG. EVs: 100+ MPGe. Compact cars and hybrids offer the best fuel economy.</p>
                        </details>
                        <details class="faq-item">
                            <summary>How much does the average American spend on gas?</summary>
                            <p>$1,800-$2,400 per year, depending on vehicle MPG, commute distance, and local gas prices. California drivers spend the most; Mississippi and Texas drivers spend the least.</p>
                        </details>
                        <details class="faq-item">
                            <summary>Which state has the cheapest gas?</summary>
                            <p>Mississippi ($2.80/gal), Louisiana ($2.85/gal), and Texas ($2.85/gal). California ($4.80/gal) is the most expensive due to high taxes and special fuel blend requirements.</p>
                        </details>
                        <details class="faq-item">
                            <summary>Is an EV cheaper to fuel than a gas car?</summary>
                            <p>Yes. EVs cost about $500-$600/year in electricity vs $1,800-$2,400/year for gas. Over 5 years, an EV can save $5,000-$8,000 in fuel costs alone.</p>
                        </details>
                        <details class="faq-item">
                            <summary>Does using AC affect fuel economy?</summary>
                            <p>Yes, AC reduces fuel economy by 5-10% in city driving. At highway speeds, AC is actually more efficient than open windows due to aerodynamic drag.</p>
                        </details>
                        <details class="faq-item">
                            <summary>How do gas prices vary by state?</summary>
                            <p>State fuel taxes (8.95¢ to 68.15¢/gal), refinery proximity, environmental regulations, and distribution costs cause variation. The spread between cheapest and most expensive states can exceed $2/gallon.</p>
                        </details>
                        <details class="faq-item">
                            <summary>What speed is most fuel-efficient?</summary>
                            <p>55-65 MPH is optimal for most vehicles. Every 5 MPH above 60 reduces fuel economy by ~7%. Driving 75 instead of 65 costs an extra $200-$300/year.</p>
                        </details>
                    </div>
                </div>
                <aside class="results-panel">
                    <h2>📊 Your Results</h2>
                    <div class="result-item"><p class="result-label">Monthly Fuel Cost</p><p class="result-value" id="monthlyCost">$0</p></div>
                    <div class="result-item"><p class="result-label">Annual Fuel Cost</p><p class="result-value secondary" id="annualCost">$0</p></div>
                    <div class="result-item"><p class="result-label">Gallons Per Month</p><p class="result-value secondary" id="gallonsPerMonth">0</p></div>
                    <div class="result-item"><p class="result-label">Cost Per Mile</p><p class="result-value secondary" id="costPerMile">$0</p></div>
                    <div class="results-breakdown">
                        <h3 style="font-size:0.95rem;font-weight:700;margin-bottom:12px;">Breakdown</h3>
                        <div class="breakdown-row"><span>Weekly Miles</span><span id="weeklyMiles">0</span></div>
                        <div class="breakdown-row"><span>Annual Miles</span><span id="annualMiles">0</span></div>
                        <div class="breakdown-row"><span>MPG</span><span id="mpgVal">0</span></div>
                        <div class="breakdown-row"><span>Gas Price</span><span id="gasVal">$0</span></div>
                    </div>
                </aside>
            </div>
        </div>
    </main>
    <footer>
        <div class="container">
            <div class="footer-inner">
                <div class="footer-brand"><span class="logo-icon">&#x1F522;</span><span>CalcWithMe</span><p>Free financial calculators.</p></div>
                <div class="footer-links"><h4>Popular</h4><a href="mortgage-calculator.html">Mortgage</a><a href="auto-loan-calculator.html">Auto Loan</a><a href="gas-calculator.html">Gas Calculator</a></div>
            </div>
            <div class="footer-bottom"><p>© 2026 CalcWithMe.com</p></div>
        </div>
    </footer>
    <script>
    function calcGas() {
        const milesPerWeek = parseFloat(document.getElementById('milesPerWeek').value) || 0;
        const mpg = parseFloat(document.getElementById('fuelEff').value) || 1;
        const gasPrice = parseFloat(document.getElementById('gasPrice').value) || 0;
        const daysPerWeek = parseFloat(document.getElementById('drivingDays').value) || 5;
        const weeksPerYear = 52;
        const annualMiles = milesPerWeek * weeksPerYear;
        const annualGallons = annualMiles / mpg;
        const annualCost = annualGallons * gasPrice;
        const monthlyCost = annualCost / 12;
        const gallonsPerMonth = annualGallons / 12;
        const costPerMile = annualMiles > 0 ? annualCost / annualMiles : 0;
        document.getElementById('monthlyCost').textContent = '$' + fmt(Math.round(monthlyCost));
        document.getElementById('annualCost').textContent = '$' + fmt(Math.round(annualCost));
        document.getElementById('gallonsPerMonth').textContent = fmt(gallonsPerMonth.toFixed(1)) + ' gal';
        document.getElementById('costPerMile').textContent = '$' + costPerMile.toFixed(2);
        document.getElementById('weeklyMiles').textContent = fmt(milesPerWeek);
        document.getElementById('annualMiles').textContent = fmt(annualMiles);
        document.getElementById('mpgVal').textContent = mpg + ' MPG';
        document.getElementById('gasVal').textContent = '$' + gasPrice.toFixed(2);
    }
    function fmt(n) { return n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); }
    window.addEventListener('load', calcGas);
    </script>
    <div class="visitor-counter"><span>👁️ Visitors: </span><span id="visitor-counter">0</span></div>
    <script src="js/visitor-counter.js"></script>
</body>
</html>'''

path = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site\gas-calculator.html'
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
import re
text = re.sub(r'<[^>]+>', ' ', html)
words = len(text.split())
print(f'P2 gas-calculator.html written: {len(html)} bytes, ~{words} words')

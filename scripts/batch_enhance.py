import os

site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

def replace_in_file(filepath, old_text, new_text):
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    if old_text not in content:
        print(f'  WARNING: old text not found in {os.path.basename(filepath)}')
        return False
    content = content.replace(old_text, new_text, 1)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

# === compound-interest-calculator.html ===
print('Processing compound-interest-calculator.html...')
f = os.path.join(site_dir, 'compound-interest-calculator.html')

replace_in_file(f,
    '<title>Compound Interest Calculator - Free Savings & Investment Growth Tool | CalcWithMe</title>',
    '<title>Free Compound Interest Calculator 2026 - Savings & Investment Growth | CalcWithMe</title>')

replace_in_file(f,
    '<meta name="description" content="Free compound interest calculator to see how your savings and investments grow over time. Model different scenarios with adjustable interest rates and contribution schedules.">',
    '<meta name="description" content="Free compound interest calculator 2026. See how your savings and investments grow with compound interest. Updated with 2026 rates and contribution limits.">')

# Read current content section
with open(f, 'r', encoding='utf-8-sig') as fh:
    content = fh.read()

old_section_start = '<h2>What is Compound Interest?</h2>'
old_section_end = '<a href="loan-calculator.html">Loan Calculator</a>\n                        </div>'
start_idx = content.find(old_section_start)
end_idx = content.find(old_section_end, start_idx)
if start_idx >= 0 and end_idx >= 0:
    end_idx += len(old_section_end)
    old_section = content[start_idx:end_idx]
    new_section = '''<h2>What is Compound Interest in 2026?</h2>
                        <p>Compound interest is interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods. Often called "interest on interest," compound interest grows your money <strong>exponentially</strong> over time. In 2026, with high-yield savings accounts offering 4-5% APY and stock market averaging 10%, understanding compound interest is more important than ever.</p>

                        <h2>The Power of Starting Early — Real Examples</h2>
                        <p><strong>Person A</strong> invests $200/month from age 25 to 35 (10 years, $24K total), then stops.</p>
                        <p><strong>Person B</strong> invests $200/month from age 35 to 65 (30 years, $72K total).</p>
                        <p>At age 65 with 7% returns: Person A has <strong>$262,000</strong>. Person B has <strong>$244,000</strong>.</p>
                        <p><strong>Person A invested 3x less but ended up with more money!</strong> That's the power of compound interest and time.</p>

                        <h2>2026 Investment Returns by Asset Class</h2>
                        <ul>
                            <li><strong>High-yield savings:</strong> 4.0–5.0% APY (FDIC insured, zero risk)</li>
                            <li><strong>Certificates of Deposit (CD):</strong> 4.0–4.5% for 12-month terms</li>
                            <li><strong>Treasury bonds:</strong> 3.5–4.5% (10-year)</li>
                            <li><strong>Corporate bonds:</strong> 5.0–6.5%</li>
                            <li><strong>S&P 500 index funds:</strong> ~10% average (historical, volatile)</li>
                            <li><strong>Real estate (REITs):</strong> 8–12% total return</li>
                        </ul>

                        <h2>The Rule of 72 — Quick Doubling Estimate</h2>
                        <p>Want to quickly estimate how long it takes to double your money? <strong>Divide 72 by your annual interest rate</strong>:</p>
                        <ul>
                            <li>At 4% return → 72 ÷ 4 = <strong>18 years</strong> to double</li>
                            <li>At 7% return → 72 ÷ 7 = <strong>10.3 years</strong> to double</li>
                            <li>At 10% return → 72 ÷ 10 = <strong>7.2 years</strong> to double</li>
                        </ul>
                        <p>This means at a 7% average return, a $10,000 investment becomes $160,000 in 40 years (doubles ~4x).</p>

                        <h2>Compound vs Simple Interest — The Difference is Huge</h2>
                        <p>For a $10,000 investment at 7% over 30 years:</p>
                        <ul>
                            <li><strong>Simple interest:</strong> $10,000 + $21,000 interest = $31,000</li>
                            <li><strong>Compound interest (monthly):</strong> $81,750</li>
                            <li><strong>Difference:</strong> Compound earns <strong>$50,750 more</strong>!</li>
                        </ul>

                        <h2>5 Mistakes That Kill Compound Growth</h2>
                        <ul>
                            <li><strong>1. Starting late</strong> — Every 5-year delay costs tens of thousands</li>
                            <li><strong>2. High fees</strong> — A 1% annual fee eats 22% of your returns over 30 years</li>
                            <li><strong>3. Not reinvesting dividends</strong> — DRIP (Dividend Reinvestment) adds 1-2% annually</li>
                            <li><strong>4. Pulling out during downturns</strong> — Missing the 10 best days in 20 years cuts returns in half</li>
                            <li><strong>5. Keeping money in low-yield accounts</strong> — 0.01% savings vs 4.5% high-yield = $4,300 difference on $10K over 10 years</li>
                        </ul>

                        <div class="related-calcs">
                            <h3>Related Calculators</h3>
                            <a href="investment-roi-calculator.html">Investment ROI Calculator</a>
                            <a href="retirement-calculator.html">Retirement Calculator</a>
                            <a href="savings-goal-calculator.html">Savings Goal Calculator</a>
                            <a href="loan-calculator.html">Loan Calculator</a>
                        </div>'''
    content = content.replace(old_section, new_section, 1)
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print('  Content section replaced')
else:
    print('  WARNING: Could not find content section boundaries')

# === retirement-calculator.html ===
print('\nProcessing retirement-calculator.html...')
f = os.path.join(site_dir, 'retirement-calculator.html')

replace_in_file(f,
    '<title>Retirement Calculator -',
    '<title>Free Retirement Calculator 2026 -')

with open(f, 'r', encoding='utf-8-sig') as fh:
    content = fh.read()

# Find content section
old_ret_start = '<h2>How Much Do You Need to Retire?</h2>'
old_ret_end_marker = '<div class="related-calcs">'
rs = content.find(old_ret_start)
re_idx = content.find(old_ret_end_marker, rs)
if rs >= 0 and re_idx >= 0:
    old_ret = content[rs:re_idx]
    new_ret = '''<h2>How Much Do You Need to Retire in 2026?</h2>
                        <p>The traditional rule of thumb suggests you need <strong>25x your annual expenses</strong> saved to retire comfortably (the 4% rule). In 2026, that means:</p>
                        <ul>
                            <li><strong>Annual expenses $40,000</strong> → Need $1,000,000 saved</li>
                            <li><strong>Annual expenses $60,000</strong> → Need $1,500,000 saved</li>
                            <li><strong>Annual expenses $80,000</strong> → Need $2,000,000 saved</li>
                            <li><strong>Annual expenses $100,000</strong> → Need $2,500,000 saved</li>
                        </ul>
                        <p>However, with inflation at 3% and healthcare costs rising, many financial planners now recommend <strong>30x annual expenses</strong> for a comfortable margin.</p>

                        <h2>2026 Retirement Account Contribution Limits</h2>
                        <ul>
                            <li><strong>401(k):</strong> $23,500/year ($31,000 if age 50+)</li>
                            <li><strong>IRA:</strong> $7,000/year ($8,000 if age 50+)</li>
                            <li><strong>Roth IRA:</strong> Same limits as traditional IRA; income limits: $161K (single) / $240K (married)</li>
                            <li><strong>HSA:</strong> $4,300/year (single) / $8,550/year (family) — triple tax advantage</li>
                        </ul>

                        <h2>Social Security in 2026: What to Expect</h2>
                        <ul>
                            <li><strong>Average monthly benefit:</strong> $1,920 ($23,040/year)</li>
                            <li><strong>Maximum benefit at full retirement age:</strong> $3,822/month</li>
                            <li><strong>Full retirement age:</strong> 67 for those born 1960+</li>
                            <li><strong>Claiming at 62:</strong> Benefits reduced by ~30%</li>
                            <li><strong>Claiming at 70:</strong> Benefits increased by ~24% vs full retirement age</li>
                            <li><strong>Key strategy:</strong> If you can afford to wait, delaying from 62 to 70 increases monthly benefit by ~77%</li>
                        </ul>

                        <h2>Retirement Savings by Age — Are You on Track?</h2>
                        <ul>
                            <li><strong>Age 30:</strong> 1x annual salary saved</li>
                            <li><strong>Age 40:</strong> 3x annual salary saved</li>
                            <li><strong>Age 50:</strong> 6x annual salary saved</li>
                            <li><strong>Age 60:</strong> 8x annual salary saved</li>
                            <li><strong>Age 67:</strong> 10x annual salary saved</li>
                        </ul>
                        <p>These are Fidelity benchmarks. If you're behind, don't panic — increase contributions by 1% each year and maximize any employer match.</p>

                        <h2>5 Common Retirement Mistakes</h2>
                        <ul>
                            <li><strong>1. Not getting the full 401(k) match</strong> — Leaving free money on the table ($1,500-5,000/year average match)</li>
                            <li><strong>2. Being too conservative</strong> — At age 30, you need growth (stocks), not just bonds</li>
                            <li><strong>3. Cashing out when changing jobs</strong> — Rolling over preserves tax advantages and avoids 10% penalty</li>
                            <li><strong>4. Underestimating healthcare costs</strong> — Fidelity estimates $315K for healthcare in retirement (couple)</li>
                            <li><strong>5. Ignoring inflation</strong> — $1M today has the purchasing power of ~$550K in 20 years at 3% inflation</li>
                        </ul>

                        '''
    content = content.replace(old_ret, new_ret, 1)
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print('  Content section replaced')
else:
    print(f'  WARNING: Could not find section boundaries (start={rs}, end={re_idx})')

# === auto-loan-calculator.html ===
print('\nProcessing auto-loan-calculator.html...')
f = os.path.join(site_dir, 'auto-loan-calculator.html')

replace_in_file(f,
    '<title>Auto Loan Calculator -',
    '<title>Free Auto Loan Calculator 2026 -')

with open(f, 'r', encoding='utf-8-sig') as fh:
    content = fh.read()

old_auto_start = '<h2>Auto Loan Basics</h2>'
old_auto_end_marker = '<div class="related-calcs">'
as_idx = content.find(old_auto_start)
ae_idx = content.find(old_auto_end_marker, as_idx)
if as_idx >= 0 and ae_idx >= 0:
    old_auto = content[as_idx:ae_idx]
    new_auto = '''<h2>Auto Loan Basics in 2026</h2>
                        <p>Auto loan rates in 2026 average <strong>6.5-7.5% for new cars</strong> and <strong>7-10% for used cars</strong>, depending on your credit score. The average new car price is $48,000, and the average loan term is 72 months.</p>
                        
                        <h2>2026 Auto Loan Rates by Credit Score</h2>
                        <ul>
                            <li><strong>Super Prime (781-850):</strong> 5.0-5.5% new / 5.5-6.5% used</li>
                            <li><strong>Prime (661-780):</strong> 6.0-7.0% new / 7.0-8.5% used</li>
                            <li><strong>Non-prime (601-660):</strong> 8.0-10.0% new / 10-13% used</li>
                            <li><strong>Subprime (501-600):</strong> 11-15% new / 15-20% used</li>
                            <li><strong>Deep subprime (300-500):</strong> 15-25%+ new / 20-25%+ used</li>
                        </ul>
                        <p><strong>Tip:</strong> Even a 50-point credit score improvement can save you $1,000-3,000 over a 5-year loan.</p>

                        <h2>New vs Used Car: Total Cost Comparison</h2>
                        <ul>
                            <li><strong>New $35K car at 6.5%, 60 months:</strong> $685/month × 60 = $41,100 total ($6,100 interest)</li>
                            <li><strong>3-year-old used $22K car at 7.5%, 60 months:</strong> $441/month × 60 = $26,460 total ($4,460 interest)</li>
                            <li><strong>Savings buying used:</strong> $14,640 + lower insurance + lower depreciation</li>
                        </ul>

                        <h2>How to Get the Best Auto Loan Rate</h2>
                        <ul>
                            <li><strong>1. Get pre-approved</strong> — Shop credit unions and online lenders before visiting the dealer</li>
                            <li><strong>2. Put 20% down on new, 10% on used</strong> — Avoid being upside-down on the loan</li>
                            <li><strong>3. Choose the shortest term you can afford</strong> — 36-48 months saves thousands in interest</li>
                            <li><strong>4. Don't finance add-ons</strong> — Extended warranties and gap insurance are cheaper bought separately</li>
                            <li><strong>5. Refinance if your score improves</strong> — Even 1% less on a $30K loan saves $800+ over the term</li>
                        </ul>

                        <h2>Avoid the 84-Month Loan Trap</h2>
                        <p>Longer loans mean lower monthly payments, but you'll pay much more in interest and likely be upside-down (owing more than the car is worth) for years. A 72-84 month loan on a depreciating asset is a recipe for negative equity.</p>

                        '''
    content = content.replace(old_auto, new_auto, 1)
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print('  Content section replaced')
else:
    print(f'  WARNING: Could not find section boundaries (start={as_idx}, end={ae_idx})')

# === savings-goal-calculator.html ===
print('\nProcessing savings-goal-calculator.html...')
f = os.path.join(site_dir, 'savings-goal-calculator.html')

replace_in_file(f,
    '<title>Savings Goal Calculator -',
    '<title>Free Savings Goal Calculator 2026 -')

with open(f, 'r', encoding='utf-8-sig') as fh:
    content = fh.read()

old_sg_start = '<h2>How to Reach Your Savings Goal</h2>'
old_sg_end_marker = '<div class="related-calcs">'
sgs = content.find(old_sg_start)
sge = content.find(old_sg_end_marker, sgs)
if sgs >= 0 and sge >= 0:
    old_sg = content[sgs:sge]
    new_sg = '''<h2>How to Reach Your Savings Goal in 2026</h2>
                        <p>Whether you're saving for a down payment, emergency fund, or dream vacation, the key is having a <strong>specific target with a deadline</strong>. Research shows that people who set specific savings goals save 2-3x more than those who just "try to save."</p>

                        <h2>Common Savings Goals and How Much to Save Monthly</h2>
                        <ul>
                            <li><strong>Emergency fund ($10K):</strong> $400/month for 25 months</li>
                            <li><strong>Down payment on $300K home (20% = $60K):</strong> $1,000/month for 5 years</li>
                            <li><strong>New car ($25K):</strong> $420/month for 5 years</li>
                            <li><strong>Wedding ($30K):</strong> $1,250/month for 2 years</li>
                            <li><strong>Vacation ($5K):</strong> $420/month for 12 months</li>
                        </ul>
                        <p>With a high-yield savings account at 4.5% APY, your money grows while you save — a $60K down payment fund earns ~$1,350/year in interest alone.</p>

                        <h2>2026 Best Places to Save Your Money</h2>
                        <ul>
                            <li><strong>High-yield savings (4-5% APY):</strong> Best for emergency funds and short-term goals (1-2 years)</li>
                            <li><strong>Certificates of Deposit (4-4.5%):</strong> Best for fixed-timeline goals; lock in rate</li>
                            <li><strong>Money market accounts (4-4.5%):</strong> Similar to HYSA with check-writing ability</li>
                            <li><strong>I-Bonds (5.27% through Oct 2026):</strong> Inflation-protected, must hold 1 year</li>
                            <li><strong>Index funds (7-10% average):</strong> Best for goals 5+ years away; higher risk but higher return</li>
                        </ul>

                        <h2>The 50/30/20 Budget Rule</h2>
                        <p>A proven framework for allocating your take-home pay:</p>
                        <ul>
                            <li><strong>50% Needs:</strong> Housing, food, insurance, minimum debt payments, utilities</li>
                            <li><strong>30% Wants:</strong> Dining out, entertainment, travel, subscriptions</li>
                            <li><strong>20% Savings:</strong> Emergency fund, retirement, extra debt payments, financial goals</li>
                        </ul>
                        <p>On a $60,000 take-home salary, that's $1,000/month toward savings goals — enough to build a $12,000 emergency fund in just 1 year.</p>

                        <h2>7 Savings Hacks That Actually Work</h2>
                        <ul>
                            <li><strong>1. Automate it</strong> — Set up auto-transfer on payday; you can't spend what you don't see</li>
                            <li><strong>2. Pay yourself first</strong> — Save before spending, not the other way around</li>
                            <li><strong>3. Use the 24-hour rule</strong> — Wait 24 hours before any non-essential purchase over $50</li>
                            <li><strong>4. Round up purchases</strong> — Apps like Acorns round up to the next dollar and invest the difference</li>
                            <li><strong>5. Track every expense</strong> — People who track spending save 15-20% more</li>
                            <li><strong>6. Increase savings with every raise</strong> — Save 50% of each raise, you won't miss it</li>
                            <li><strong>7. Cancel 1 subscription per month</strong> — Average savings: $50-200/month</li>
                        </ul>

                        '''
    content = content.replace(old_sg, new_sg, 1)
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print('  Content section replaced')
else:
    print(f'  WARNING: Could not find section boundaries (start={sgs}, end={sge})')

# === loan-calculator.html ===
print('\nProcessing loan-calculator.html...')
f = os.path.join(site_dir, 'loan-calculator.html')

replace_in_file(f,
    '<title>Loan Calculator -',
    '<title>Free Loan Calculator 2026 -')

with open(f, 'r', encoding='utf-8-sig') as fh:
    content = fh.read()

old_loan_start = '<h2>How Loan Payments Work</h2>'
old_loan_end_marker = '<div class="related-calcs">'
ls = content.find(old_loan_start)
le = content.find(old_loan_end_marker, ls)
if ls >= 0 and le >= 0:
    old_loan = content[ls:le]
    new_loan = '''<h2>How Loan Payments Work in 2026</h2>
                        <p>Every loan payment has two parts: <strong>principal</strong> (reducing what you owe) and <strong>interest</strong> (the cost of borrowing). In the early years, most of your payment goes to interest. Over time, more goes to principal — this is called <strong>amortization</strong>.</p>

                        <h2>2026 Loan Rates by Type</h2>
                        <ul>
                            <li><strong>Personal loan (good credit):</strong> 7-12%</li>
                            <li><strong>Personal loan (fair credit):</strong> 13-20%</li>
                            <li><strong>Auto loan (new):</strong> 5-7%</li>
                            <li><strong>Auto loan (used):</strong> 7-10%</li>
                            <li><strong>Mortgage (30-year fixed):</strong> 6.5-7.0%</li>
                            <li><strong>Mortgage (15-year fixed):</strong> 5.8-6.3%</li>
                            <li><strong>Student loan (federal):</strong> 5.50-8.05%</li>
                            <li><strong>Student loan (private):</strong> 4-15%</li>
                            <li><strong>Home equity loan:</strong> 7-9%</li>
                            <li><strong>HELOC:</strong> 7.5-9.5% (variable)</li>
                        </ul>

                        <h2>Amortization: Why Early Payments Are Mostly Interest</h2>
                        <p>On a $300,000 mortgage at 6.5% for 30 years ($1,896/month):</p>
                        <ul>
                            <li><strong>Month 1:</strong> $1,625 interest / $271 principal (86% interest!)</li>
                            <li><strong>Year 5:</strong> $1,500 interest / $396 principal</li>
                            <li><strong>Year 15:</strong> $1,100 interest / $796 principal</li>
                            <li><strong>Year 25:</strong> $500 interest / $1,396 principal</li>
                        </ul>
                        <p><strong>Tip:</strong> Making just 1 extra payment per year on a 30-year mortgage pays it off 4 years early and saves $40,000+ in interest.</p>

                        <h2>How to Get the Best Loan Rate</h2>
                        <ul>
                            <li><strong>1. Improve your credit score</strong> — Going from 680 to 760 can save 1-2% on most loan types</li>
                            <li><strong>2. Shop at least 3 lenders</strong> — Rates can vary 1-3% between lenders for the same borrower</li>
                            <li><strong>3. Shorter term = lower rate</strong> — 15-year mortgage rates are typically 0.5-1% lower than 30-year</li>
                            <li><strong>4. Put more down</strong> — 20% down on a mortgage avoids PMI ($100-300/month)</li>
                            <li><strong>5. Consider credit unions</strong> — Often offer 0.5-1.5% lower rates than big banks</li>
                        </ul>

                        <h2>Warning Signs of a Bad Loan</h2>
                        <ul>
                            <li><strong>Prepayment penalties</strong> — You shouldn't be charged for paying off early</li>
                            <li><strong>Variable rate with no cap</strong> — Your payment could double if rates rise</li>
                            <li><strong>APR much higher than advertised rate</strong> — APR includes fees; a big gap means hidden costs</li>
                            <li><strong>Pushed add-on products</strong> — Credit insurance, GAP coverage often overpriced at dealers</li>
                        </ul>

                        '''
    content = content.replace(old_loan, new_loan, 1)
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print('  Content section replaced')
else:
    print(f'  WARNING: Could not find section boundaries (start={ls}, end={le})')

print('\nDone!')

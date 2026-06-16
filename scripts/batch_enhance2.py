import os

site_dir = r'C:\Users\Administrator\.qclaw\workspace\calcwithme-site'

def replace_section(filepath, start_marker, end_marker, new_content):
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx + len(start_marker))
    if start_idx < 0 or end_idx < 0:
        print(f'  WARNING: markers not found (start={start_idx}, end={end_idx})')
        return False
    old = content[start_idx:end_idx]
    content = content[:start_idx] + new_content + content[end_idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Replaced {len(old)} chars with {len(new_content)} chars')
    return True

# === auto-loan-calculator.html ===
print('Processing auto-loan-calculator.html...')
f = os.path.join(site_dir, 'auto-loan-calculator.html')
replace_section(f,
    '<h2>How Auto Loan Financing Works</h2>',
    '<div class="related-calcs">',
    '''<h2>How Auto Loan Financing Works in 2026</h2>
                        <p>When you finance a car, you borrow money from a lender to pay for the vehicle. You repay the loan with interest over a set period. In 2026, <strong>average auto loan rates are 6.5-7.5% for new cars</strong> and <strong>7-10% for used cars</strong>, depending on your credit score. The average new car price is $48,000.</p>
                        
                        <h2>2026 Auto Loan Rates by Credit Score</h2>
                        <ul>
                            <li><strong>Super Prime (781-850):</strong> 5.0-5.5% new / 5.5-6.5% used</li>
                            <li><strong>Prime (661-780):</strong> 6.0-7.0% new / 7.0-8.5% used</li>
                            <li><strong>Non-prime (601-660):</strong> 8.0-10.0% new / 10-13% used</li>
                            <li><strong>Subprime (501-600):</strong> 11-15% new / 15-20% used</li>
                        </ul>

                        <h2>New vs Used Car: Total Cost Comparison</h2>
                        <ul>
                            <li><strong>New $35K car at 6.5%, 60 months:</strong> $685/month, $41,100 total ($6,100 interest)</li>
                            <li><strong>3-year-old used $22K at 7.5%, 60 months:</strong> $441/month, $26,460 total ($4,460 interest)</li>
                            <li><strong>Savings buying used:</strong> $14,640 + lower insurance + lower depreciation</li>
                        </ul>

                        <h2>5 Tips to Get the Best Auto Loan Rate</h2>
                        <ul>
                            <li><strong>1. Get pre-approved</strong> — Shop credit unions and online lenders before visiting the dealer</li>
                            <li><strong>2. Put 20% down on new, 10% on used</strong> — Avoid being upside-down on the loan</li>
                            <li><strong>3. Choose the shortest term you can afford</strong> — 36-48 months saves thousands in interest</li>
                            <li><strong>4. Don't finance add-ons at the dealer</strong> — Extended warranties and gap insurance are cheaper bought separately</li>
                            <li><strong>5. Refinance if your score improves</strong> — Even 1% less on a $30K loan saves $800+</li>
                        </ul>

                        <h2>Avoid the 84-Month Loan Trap</h2>
                        <p>Longer loans mean lower monthly payments, but you'll pay much more in interest and likely be upside-down (owing more than the car is worth) for years. A 72-84 month loan on a depreciating asset is a recipe for negative equity.</p>

                        <div class="related-calcs">''')

# === savings-goal-calculator.html ===
print('Processing savings-goal-calculator.html...')
f = os.path.join(site_dir, 'savings-goal-calculator.html')
replace_section(f,
    '<h2>How to Reach Your Savings Goals</h2>',
    '<div class="related-calcs">',
    '''<h2>How to Reach Your Savings Goals in 2026</h2>
                        <p>Whether you're saving for a down payment, emergency fund, or dream vacation, the key is having a <strong>specific target with a deadline</strong>. Research shows that people who set specific savings goals save 2-3x more than those who just "try to save." With high-yield savings accounts offering 4-5% APY in 2026, your money grows while you save.</p>

                        <h2>Common Savings Goals — Monthly Amounts Needed</h2>
                        <ul>
                            <li><strong>Emergency fund ($10K):</strong> $400/month for 25 months</li>
                            <li><strong>Down payment on $300K home (20% = $60K):</strong> $1,000/month for 5 years</li>
                            <li><strong>New car ($25K):</strong> $420/month for 5 years</li>
                            <li><strong>Wedding ($30K):</strong> $1,250/month for 2 years</li>
                            <li><strong>Vacation ($5K):</strong> $420/month for 12 months</li>
                        </ul>

                        <h2>2026 Best Places to Save Your Money</h2>
                        <ul>
                            <li><strong>High-yield savings (4-5% APY):</strong> Best for emergency funds and short-term goals</li>
                            <li><strong>Certificates of Deposit (4-4.5%):</strong> Best for fixed-timeline goals; lock in rate</li>
                            <li><strong>Money market accounts (4-4.5%):</strong> Similar to HYSA with check-writing ability</li>
                            <li><strong>I-Bonds (5.27% through Oct 2026):</strong> Inflation-protected, must hold 1 year</li>
                            <li><strong>Index funds (7-10% average):</strong> Best for goals 5+ years away; higher risk but higher return</li>
                        </ul>

                        <h2>The 50/30/20 Budget Rule</h2>
                        <ul>
                            <li><strong>50% Needs:</strong> Housing, food, insurance, minimum debt payments, utilities</li>
                            <li><strong>30% Wants:</strong> Dining out, entertainment, travel, subscriptions</li>
                            <li><strong>20% Savings:</strong> Emergency fund, retirement, extra debt payments, financial goals</li>
                        </ul>
                        <p>On a $60,000 take-home salary, that's $1,000/month toward savings — enough to build a $12,000 emergency fund in 1 year.</p>

                        <h2>7 Savings Hacks That Actually Work</h2>
                        <ul>
                            <li><strong>1. Automate it</strong> — Set up auto-transfer on payday; you can't spend what you don't see</li>
                            <li><strong>2. Pay yourself first</strong> — Save before spending, not the other way around</li>
                            <li><strong>3. Use the 24-hour rule</strong> — Wait 24 hours before any non-essential purchase over $50</li>
                            <li><strong>4. Round up purchases</strong> — Apps round up to the next dollar and invest the difference</li>
                            <li><strong>5. Track every expense</strong> — People who track spending save 15-20% more</li>
                            <li><strong>6. Increase savings with every raise</strong> — Save 50% of each raise; you won't miss it</li>
                            <li><strong>7. Cancel 1 subscription per month</strong> — Average savings: $50-200/month</li>
                        </ul>

                        <div class="related-calcs">''')

# === loan-calculator.html ===
print('Processing loan-calculator.html...')
f = os.path.join(site_dir, 'loan-calculator.html')
replace_section(f,
    '<h2>How to Use This Loan Calculator</h2>',
    '<div class="related-calcs">',
    '''<h2>How Loan Payments Work in 2026</h2>
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
                            <li><strong>1. Improve your credit score</strong> — Going from 680 to 760 can save 1-2% on most loans</li>
                            <li><strong>2. Shop at least 3 lenders</strong> — Rates can vary 1-3% for the same borrower</li>
                            <li><strong>3. Shorter term = lower rate</strong> — 15-year mortgage rates are 0.5-1% lower than 30-year</li>
                            <li><strong>4. Put more down</strong> — 20% down on a mortgage avoids PMI ($100-300/month)</li>
                            <li><strong>5. Consider credit unions</strong> — Often offer 0.5-1.5% lower rates than big banks</li>
                        </ul>

                        <h2>Warning Signs of a Bad Loan</h2>
                        <ul>
                            <li><strong>Prepayment penalties</strong> — You shouldn't be charged for paying off early</li>
                            <li><strong>Variable rate with no cap</strong> — Your payment could double if rates rise</li>
                            <li><strong>APR much higher than advertised rate</strong> — Big gap means hidden costs</li>
                            <li><strong>Pushed add-on products</strong> — Credit insurance, GAP coverage often overpriced at dealers</li>
                        </ul>

                        <div class="related-calcs">''')

print('\nDone!')

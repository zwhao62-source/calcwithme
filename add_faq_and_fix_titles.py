# -*- coding: utf-8 -*-
"""
批量为计算器页面添加FAQ并优化标题
"""
import os
import re

SITE_DIR = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"

# 每个计算器对应的FAQ数据
FAQ_DATA = {
    "loan-calculator.html": {
        "title": "Loan Calculator - Free Online Personal Loan Calculator | CalcWithMe",
        "h1": "Loan Calculator",
        "description": "Free personal loan calculator to estimate monthly payments, total interest, and amortization schedule. Compare different loan scenarios instantly.",
        "faqs": [
            ("How does a loan calculator help me?", "Our loan calculator helps you estimate monthly payments based on loan amount, interest rate, and term. It also shows total interest paid and the full amortization schedule so you can plan your finances better."),
            ("What is a good interest rate for a personal loan?", "As of 2026, competitive personal loan rates range from 8% to 15% APR depending on your credit score. Those with excellent credit (740+) may qualify for rates as low as 6-8%, while borrowers with fair credit (640-699) typically see rates of 15-22%."),
            ("How is interest calculated on a loan?", "Loan interest is calculated monthly based on the remaining principal balance. Early in the loan, more of your payment goes to interest. As you pay down the principal, the interest portion decreases and more goes to principal."),
            ("What is an amortization schedule?", "An amortization schedule shows how each payment is split between principal and interest over the life of the loan. It also shows your remaining balance after each payment, helping you track how fast you're paying off debt."),
            ("Should I choose a shorter loan term?", "Shorter loan terms mean higher monthly payments but significantly less total interest paid. For example, a 3-year loan at 10% APR costs much less in total interest than a 6-year loan at the same rate. Choose based on your budget comfort level."),
            ("What's the difference between secured and unsecured loans?", "Secured loans require collateral (like a car or savings account) and typically offer lower rates. Unsecured loans don't require collateral but have higher rates and stricter credit requirements."),
        ]
    },
    "auto-loan-calculator.html": {
        "title": "Auto Loan Calculator - Free Car Loan Payment Calculator | CalcWithMe",
        "h1": "Auto Loan Calculator",
        "description": "Free car loan calculator to estimate monthly payments, total interest, and compare dealer financing vs bank loans. Save money on your next vehicle purchase.",
        "faqs": [
            ("How is my auto loan monthly payment calculated?", "Your monthly payment is based on the loan amount (vehicle price minus down payment), annual interest rate, and loan term (typically 36-84 months). Longer terms lower payments but increase total interest paid."),
            ("What credit score do I need for the best auto loan rates?", "A credit score of 720+ typically qualifies for the best rates (as low as 5-7% APR for new cars). Scores of 660-719 may get 8-12%, while scores below 660 often see rates above 12% or may require a co-signer."),
            ("How much should I put down on a car?", "A down payment of 10-20% of the vehicle's value is recommended. A larger down payment reduces the loan amount, lowers your monthly payment, and can help you qualify for better rates."),
            ("New car vs used car: which is better for financing?", "New cars offer lower rates (often 0-5% promotional financing from dealers) but depreciate faster. Used cars (2-3 years old) offer better value, lower insurance costs, and similar reliability at a lower price point."),
            ("Should I get pre-approved before visiting a dealership?", "Yes! Getting pre-approved by a bank or credit union before visiting dealerships gives you negotiating power, reveals your true budget, and often results in better rates than dealer financing."),
        ]
    },
    "compound-interest-calculator.html": {
        "title": "Compound Interest Calculator - Free Savings & Investment Growth Tool | CalcWithMe",
        "h1": "Compound Interest Calculator",
        "description": "Free compound interest calculator to see how your savings and investments grow over time. Model different scenarios with adjustable interest rates and contribution schedules.",
        "faqs": [
            ("What is compound interest and why does it matter?", "Compound interest is interest earned on both your initial principal and accumulated interest. Albert Einstein reportedly called it the 'eighth wonder of the world.' Over time, compound interest creates exponential growth, making it your most powerful wealth-building tool."),
            ("How often should I compound my savings?", "More frequent compounding (daily or monthly) generates slightly more returns than annual compounding. With modern savings accounts and investments, compounding typically occurs monthly. The difference is small but adds up over decades."),
            ("What is the difference between simple and compound interest?", "Simple interest is calculated only on the principal amount. Compound interest includes accumulated interest in each calculation. For a $10,000 investment at 5% over 20 years: simple interest = $10,000, compound interest = $26,533."),
            ("How much can I earn with compound interest over 10 years?", "Example: $10,000 invested at 7% annual return with $200/month contributions = approximately $53,000 after 10 years (vs $24,000 with no growth). Use our calculator to model your specific scenario."),
            ("What is a realistic expected investment return?", "Historical average annual returns: S&P 500 index funds ~10%, bonds ~5%, high-yield savings ~4-5%. Remember that past performance doesn't guarantee future results. Factor in inflation (historically ~3%)."),
            ("How do regular contributions affect compound growth?", "Regular contributions dramatically increase compound growth. Example: $10,000 initial + $500/month at 8% for 20 years = ~$298,000. Without contributions, the same initial amount grows to only ~$46,600."),
        ]
    },
    "credit-card-payoff-calculator.html": {
        "title": "Credit Card Payoff Calculator - Free Debt Payoff Planner | CalcWithMe",
        "h1": "Credit Card Payoff Calculator",
        "description": "Free credit card payoff calculator to plan your debt-free journey. Compare avalanche vs snowball methods and see exactly when you'll be debt-free.",
        "faqs": [
            ("What is the fastest way to pay off credit card debt?", "The two main methods are: (1) Avalanche Method - pay minimums on all cards, put extra money toward the highest APR card. (2) Snowball Method - pay minimums on all cards, put extra money toward the smallest balance first. Avalanche saves the most money; Snowball provides psychological wins."),
            ("How much should I pay monthly on my credit card?", "Always pay more than the minimum payment. If you only pay minimums on a $5,000 balance at 20% APR with a 2% minimum, it takes 26 years and costs $7,500 in interest! Even doubling the minimum payment dramatically reduces total cost."),
            ("Should I use a balance transfer card?", "Balance transfer cards with 0% APR promotional periods (12-21 months) can save thousands in interest. Watch out for transfer fees (typically 3-5%) and have a plan to pay off the balance before the promo ends."),
            ("How does minimum payment calculation work?", "Credit card minimums are typically 1-2% of the balance plus any interest accrued, or a fixed amount (usually $25-35), whichever is greater. Use our calculator to see how minimum payments keep you in debt."),
            ("What is the difference between APR and APY for credit cards?", "Credit card APR (Annual Percentage Rate) is the stated interest rate. Since credit cards compound daily, the effective APY (Annual Percentage Yield) is higher. For example, 20% APR ≈ 22% APY when compounded daily."),
        ]
    },
    "investment-roi-calculator.html": {
        "title": "Investment ROI Calculator - Free Return on Investment Calculator | CalcWithMe",
        "h1": "Investment ROI Calculator",
        "description": "Free ROI calculator to measure your investment returns, compare opportunities, and make data-driven investment decisions with clear profit/loss analysis.",
        "faqs": [
            ("How do I calculate return on investment (ROI)?", "ROI = (Current Value - Initial Investment) / Initial Investment × 100%. For example: invested $10,000, now worth $12,500, ROI = ($12,500 - $10,000) / $10,000 × 100% = 25%."),
            ("What is a good ROI percentage?", "A 'good' ROI depends on the investment type and risk level. Savings accounts: 4-5%, Bonds: 5-7%, Stocks: 7-10% historically. Real estate: 8-12%. High-risk investments should yield 15%+. Always compare similar-risk investments."),
            ("What's the difference between ROI and annualized return?", "ROI measures total return over an entire period. Annualized return (CAGR) measures the average yearly return as if growth was steady. A 50% ROI over 5 years = 8.45% annualized return, which is more useful for comparison."),
            ("How do fees affect my investment returns?", "Fees compound against you. A 1% annual fee reduces a 30-year portfolio by ~22%. A 2% fee reduces it by ~40%. Always compare net returns (after fees) when evaluating investments."),
            ("Should I calculate ROI before or after taxes?", "Always calculate pre-tax ROI first. After-tax ROI depends on your income bracket, investment type (taxable vs tax-advantaged), and how long you hold. Tax-advantaged accounts (401k, IRA) can dramatically improve after-tax returns."),
        ]
    },
    "retirement-calculator.html": {
        "title": "Retirement Calculator - Free Retirement Planning Tool | CalcWithMe",
        "h1": "Retirement Calculator",
        "description": "Free retirement calculator to plan your retirement savings, estimate how much you need, and see if you're on track to meet your retirement goals.",
        "faqs": [
            ("How much do I need to retire?", "A common rule is to save 25× your annual expenses (based on the 4% safe withdrawal rate). If you spend $50,000/year, you need ~$1.25 million. Adjust based on your expected retirement lifestyle, healthcare costs, and Social Security benefits."),
            ("How much should I contribute to my 401(k)?", "Contribute at least enough to get your full employer match (it's free money!). After that, max out a Roth IRA ($7,000/year in 2024). Then maximize 401(k) ($23,000/year limit). Aim to save 15-20% of your income total."),
            ("What is the 4% rule?", "The 4% rule suggests you can withdraw 4% of your portfolio in year one of retirement, then adjust for inflation. This historically gave retirees a 30-year fund. Many experts now suggest 3.3-3.5% for greater safety given longer lifespans."),
            ("When should I start saving for retirement?", "Start as early as possible! Starting at 25 vs 35 to reach $1M by 65: starting at 25 requires ~$300/month; starting at 35 requires ~$700/month. Time in the market beats timing the market."),
            ("What about Social Security?", "Social Security replaces about 40% of pre-retirement income for average earners. The optimal claiming age depends on your health, financial needs, and spouse's benefits. Claiming at 70 maximizes benefits (8% increase/year after full retirement age)."),
        ]
    },
    "rent-vs-buy-calculator.html": {
        "title": "Rent vs Buy Calculator - Should You Rent or Buy a Home? | CalcWithMe",
        "h1": "Rent vs Buy Calculator",
        "description": "Free rent vs buy calculator to make the rent vs buy decision based on real numbers. Consider down payment, mortgage rates, maintenance, and opportunity cost.",
        "faqs": [
            ("Is it better to rent or buy a home?", "The rent vs buy decision depends on: how long you plan to stay (typically 5+ years favors buying), current mortgage rates vs rent prices, your financial situation, and local market conditions. Use our calculator to run the numbers for your specific situation."),
            ("What is the '5-year rule' for buying a home?", "The 5-year rule suggests you should stay in a home for at least 5 years to recoup closing costs (typically 2-5% of home price), moving costs, and the initial investment. Shorter stays often favor renting."),
            ("What costs should I consider when buying?", "Beyond the down payment, budget for: closing costs (2-5%), moving costs, ongoing maintenance (1-2% of home value/year), property taxes, homeowners insurance, HOA fees, and property management if applicable."),
            ("How does homeownership build wealth?", "Homeownership builds wealth through: (1) Equity - paying down the mortgage, (2) Appreciation - home value increases over time (~3-5% historically), (3) Locked-in housing costs - fixed-rate mortgage doesn't increase with inflation, unlike rent."),
            ("What about the opportunity cost of a down payment?", "Money invested in a down payment could alternatively be invested in the stock market. Historically, investing the 20% down payment in a diversified portfolio has outperformed homeownership in many markets, especially shorter timeframes."),
        ]
    },
    "salary-calculator.html": {
        "title": "Salary Calculator - Hourly to Annual Salary Converter | CalcWithMe",
        "h1": "Salary Calculator",
        "description": "Free salary calculator to convert hourly wage to annual salary, estimate take-home pay after taxes, and compare job offers with different pay structures.",
        "faqs": [
            ("How do I convert hourly wage to annual salary?", "Annual salary = Hourly rate × Hours per week × 52 weeks. Full-time (40 hrs/week): multiply hourly rate by 2,080. Part-time (20 hrs/week): multiply by 1,040. Don't forget to account for unpaid vacation and holidays."),
            ("What's the difference between gross and net pay?", "Gross pay is your total before deductions. Net pay (take-home pay) is what you receive after: federal income tax, state income tax, Social Security (6.2%), Medicare (1.45%), health insurance premiums, and retirement contributions."),
            ("How are federal taxes calculated on salary?", "Federal taxes use progressive brackets. In 2024, brackets range from 10% to 37% depending on taxable income. Your marginal rate applies to each additional dollar earned. Deductions (401k, IRA, etc.) reduce your taxable income."),
            ("How many hours per year do full-time workers work?", "Full-time = 40 hours/week × 52 weeks = 2,080 hours/year. Accounting for 10 federal holidays + average 10 vacation days = 2,000 billable hours. For salary negotiations, use 2,080 hours."),
            ("Should I negotiate salary or benefits?", "Always negotiate! A $5,000 salary increase compounds over your entire career and affects retirement contributions. But also consider: health insurance quality, 401k match, bonuses, remote work options, and professional development budget."),
        ]
    },
    "savings-goal-calculator.html": {
        "title": "Savings Goal Calculator - Free Goal-Based Savings Planner | CalcWithMe",
        "h1": "Savings Goal Calculator",
        "description": "Free savings goal calculator to plan how much to save monthly to reach your financial goals. Whether it's an emergency fund, vacation, or down payment - we'll show you the path.",
        "faqs": [
            ("How much should I save each month for my goal?", "Use the formula: Monthly savings = (Goal amount) / Months until goal. Example: $10,000 in 24 months = ~$417/month. Add a buffer for unexpected events. Automating savings makes consistent progress easier."),
            ("What is a realistic savings rate?", "Financial experts recommend saving 20% of your income. A good starting target: 3 months of expenses for emergency fund, then shift to retirement and specific goals. Even 10-15% is a solid start - the key is starting now."),
            ("Where should I keep my savings?", "Emergency fund: High-yield savings account (4-5% APY, FDIC insured). Short-term goals (1-3 years): High-yield savings or CDs. Long-term goals (5+ years): Consider index funds for growth potential, accepting some risk."),
            ("How do I prioritize multiple savings goals?", "Priority order: (1) Emergency fund first ($1,000 starter, then 3-6 months expenses), (2) High-interest debt payoff, (3) Employer 401k match, (4) Other goals. Focus on one goal at a time while maintaining minimums on others."),
            ("How can I save more with a tight budget?", "Strategies: Track every expense for one month, automate savings on payday, cut one subscription, try a 'no-spend' challenge, negotiate bills, cancel unused memberships, use cashback apps. Small changes compound into significant savings."),
        ]
    },
}

FAQ_HTML_TEMPLATE = """
                        
                        <!-- FAQ Section for SEO -->
                        <div class="faq-section">
                            <h3>Frequently Asked Questions</h3>
                            {faqs}
                        </div>
                    </div>
                </div>
"""

FAQ_ITEM_TEMPLATE = """
                            <details class="faq-item">
                                <summary>{question}</summary>
                                <p>{answer}</p>
                            </details>
"""

def build_faq_section(faqs):
    faq_items = ""
    for q, a in faqs:
        faq_items += FAQ_ITEM_TEMPLATE.format(question=q, answer=a)
    return FAQ_HTML_TEMPLATE.format(faqs=faq_items)

def fix_file(filepath, data):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original = content
    
    # Fix title
    old_title_match = re.search(r'<title>([^<]+)</title>', content)
    if old_title_match:
        old_title = old_title_match.group(0)
        new_title = '<title>' + data['title'] + '</title>'
        content = content.replace(old_title, new_title)
        print("  [TITLE] {} -> {}".format(old_title_match.group(1), data['title']))
    
    # Fix meta description
    old_desc_match = re.search(r'<meta name="description" content="[^"]*"', content)
    if old_desc_match:
        old_desc = old_desc_match.group(0)
        new_desc = '<meta name="description" content="' + data['description'] + '"'
        content = content.replace(old_desc, new_desc)
        print("  [DESC] Updated meta description")
    
    # Add FAQ section if not present
    if 'faq' not in content.lower() or '<details' not in content:
        # Find insertion point: before </div> that closes the main content panel
        # We look for the results sidebar marker and insert FAQ before it
        faq_html = build_faq_section(data['faqs'])
        
        # Try to insert before the results sidebar or footer
        insert_patterns = [
            '<!-- Results Sidebar -->',
            '<aside class="results-panel"',
            '<footer>',
            '</main>',
        ]
        
        inserted = False
        for pattern in insert_patterns:
            if pattern in content:
                # Find the first occurrence
                idx = content.index(pattern)
                # Insert just before this pattern, but after some content
                # Look for the last </div> before this pattern
                search_start = max(0, idx - 200)
                before = content[search_start:idx]
                last_div = before.rfind('</div>')
                if last_div >= 0:
                    insert_point = search_start + last_div + 6
                    content = content[:insert_point] + faq_html + content[insert_point:]
                    inserted = True
                    print("  [FAQ] Added FAQ section (before: {})".format(pattern[:30]))
                    break
        
        if not inserted:
            print("  [FAQ] Could not find insertion point - skipping")
    else:
        print("  [FAQ] Already has FAQ content - skipping")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("=" * 60)
    print("批量添加FAQ & 优化标题")
    print("=" * 60)
    
    modified = []
    for filename, data in FAQ_DATA.items():
        filepath = os.path.join(SITE_DIR, filename)
        if not os.path.exists(filepath):
            print("[SKIP] {} - 文件不存在".format(filename))
            continue
        
        print("\n处理: {}".format(filename))
        changed = fix_file(filepath, data)
        if changed:
            modified.append(filename)
    
    print("\n" + "=" * 60)
    print("完成！修改了 {} 个文件".format(len(modified)))
    for f in modified:
        print("  - {}".format(f))
    print("=" * 60)

if __name__ == "__main__":
    main()

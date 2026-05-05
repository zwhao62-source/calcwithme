# -*- coding: utf-8 -*-
"""
为计算器页面添加 FAQ JSON-LD Schema
"""
import os
import re
import json

SITE_DIR = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"

# 每个页面对应的 FAQ 数据
FAQ_SCHEMA_DATA = {
    "mortgage-calculator.html": {
        "questions": [
            {"question": "How much house can I afford with a $4,000 monthly payment?", "answer": "With a $4,000 monthly mortgage payment (including taxes and insurance) at a 6.5% interest rate on a 30-year loan, you could afford approximately a $500,000-$550,000 home with a 20% down payment."},
            {"question": "What is a good mortgage interest rate in 2026?", "answer": "As of 2026, a competitive 30-year fixed mortgage rate ranges from 6.3% to 6.8% depending on your credit score, down payment, and lender."},
            {"question": "Should I choose a 15-year or 30-year mortgage?", "answer": "Choose a 15-year mortgage if you want to pay off your home faster and save on total interest (typically 50-60% less). Choose a 30-year mortgage if you need lower monthly payments."},
            {"question": "How much down payment do I need?", "answer": "While you can put down as little as 3-5% with some loan programs, putting down 20% or more helps you avoid PMI and get better interest rates."},
            {"question": "What is PMI?", "answer": "PMI (Private Mortgage Insurance) is required when your down payment is less than 20%. It typically costs 0.3-1.5% of your loan amount annually."}
        ]
    },
    "loan-calculator.html": {
        "questions": [
            {"question": "How does a loan calculator help me?", "answer": "Our loan calculator helps you estimate monthly payments based on loan amount, interest rate, and term. It also shows total interest paid and the full amortization schedule."},
            {"question": "What is a good interest rate for a personal loan?", "answer": "As of 2026, competitive personal loan rates range from 8% to 15% APR depending on your credit score."},
            {"question": "How is interest calculated on a loan?", "answer": "Loan interest is calculated monthly based on the remaining principal balance. Early in the loan, more of your payment goes to interest."},
            {"question": "What is an amortization schedule?", "answer": "An amortization schedule shows how each payment is split between principal and interest over the life of the loan."}
        ]
    },
    "auto-loan-calculator.html": {
        "questions": [
            {"question": "How is my auto loan monthly payment calculated?", "answer": "Your monthly payment is based on the loan amount, annual interest rate, and loan term (typically 36-84 months)."},
            {"question": "What credit score do I need for the best auto loan rates?", "answer": "A credit score of 720+ typically qualifies for the best rates (as low as 5-7% APR for new cars)."},
            {"question": "How much should I put down on a car?", "answer": "A down payment of 10-20% of the vehicle's value is recommended."},
            {"question": "Should I get pre-approved before visiting a dealership?", "answer": "Yes! Getting pre-approved by a bank or credit union before visiting dealerships gives you negotiating power."}
        ]
    },
    "compound-interest-calculator.html": {
        "questions": [
            {"question": "What is compound interest and why does it matter?", "answer": "Compound interest is interest earned on both your initial principal and accumulated interest. Over time, it creates exponential growth."},
            {"question": "How often should I compound my savings?", "answer": "More frequent compounding (daily or monthly) generates slightly more returns than annual compounding."},
            {"question": "What is the difference between simple and compound interest?", "answer": "Simple interest is calculated only on the principal amount. Compound interest includes accumulated interest in each calculation."},
            {"question": "How much can I earn with compound interest over 10 years?", "answer": "Example: $10,000 invested at 7% annual return with $200/month contributions = approximately $53,000 after 10 years."}
        ]
    },
    "credit-card-payoff-calculator.html": {
        "questions": [
            {"question": "What is the fastest way to pay off credit card debt?", "answer": "The two main methods are: Avalanche Method (pay highest APR first) and Snowball Method (pay smallest balance first)."},
            {"question": "How much should I pay monthly on my credit card?", "answer": "Always pay more than the minimum payment. If you only pay minimums, it can take 26 years to pay off!"},
            {"question": "Should I use a balance transfer card?", "answer": "Balance transfer cards with 0% APR promotional periods (12-21 months) can save thousands in interest."}
        ]
    },
    "investment-roi-calculator.html": {
        "questions": [
            {"question": "How do I calculate return on investment (ROI)?", "answer": "ROI = (Current Value - Initial Investment) / Initial Investment x 100%."},
            {"question": "What is a good ROI percentage?", "answer": "A good ROI depends on the investment type and risk level. Stocks: 7-10% historically, Bonds: 5-7%."},
            {"question": "How do fees affect my investment returns?", "answer": "A 1% annual fee reduces a 30-year portfolio by approximately 22%."}
        ]
    },
    "retirement-calculator.html": {
        "questions": [
            {"question": "How much do I need to retire?", "answer": "A common rule is to save 25x your annual expenses. If you spend $50,000/year, you need approximately $1.25 million."},
            {"question": "How much should I contribute to my 401(k)?", "answer": "Contribute at least enough to get your full employer match. After that, max out a Roth IRA ($7,000/year)."},
            {"question": "What is the 4% rule?", "answer": "The 4% rule suggests you can withdraw 4% of your portfolio in year one of retirement, then adjust for inflation."}
        ]
    },
    "rent-vs-buy-calculator.html": {
        "questions": [
            {"question": "Is it better to rent or buy a home?", "answer": "The rent vs buy decision depends on how long you plan to stay (typically 5+ years favors buying), current mortgage rates vs rent prices."},
            {"question": "What is the 5-year rule for buying a home?", "answer": "The 5-year rule suggests you should stay in a home for at least 5 years to recoup closing costs."},
            {"question": "What costs should I consider when buying?", "answer": "Beyond the down payment, budget for: closing costs (2-5%), moving costs, ongoing maintenance (1-2% of home value/year)."}
        ]
    },
    "salary-calculator.html": {
        "questions": [
            {"question": "How do I convert hourly wage to annual salary?", "answer": "Annual salary = Hourly rate x Hours per week x 52 weeks. Full-time (40 hrs/week): multiply by 2,080."},
            {"question": "What is the difference between gross and net pay?", "answer": "Gross pay is your total before deductions. Net pay is what you receive after: federal tax, state tax, Social Security, Medicare."},
            {"question": "How are federal taxes calculated on salary?", "answer": "Federal taxes use progressive brackets ranging from 10% to 37% depending on taxable income."}
        ]
    },
    "savings-goal-calculator.html": {
        "questions": [
            {"question": "How much should I save each month for my goal?", "answer": "Use the formula: Monthly savings = (Goal amount) / Months until goal."},
            {"question": "What is a realistic savings rate?", "answer": "Financial experts recommend saving 20% of your income. A good starting target: 3 months of expenses for emergency fund."},
            {"question": "Where should I keep my savings?", "answer": "Emergency fund: High-yield savings account (4-5% APY). Short-term goals: High-yield savings or CDs."}
        ]
    }
}

def add_faq_schema(filepath, data):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check if already has FAQ schema
    if '"FAQPage"' in content or '"@type": "Question"' in content:
        print(f"  [SKIP] Already has FAQ schema")
        return False
    
    # Build FAQ JSON-LD
    faq_json = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }
    
    for q in data["questions"]:
        faq_json["mainEntity"].append({
            "@type": "Question",
            "name": q["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": q["answer"]
            }
        })
    
    # Insert after existing ld+json or before </head>
    schema_script = f'<script type="application/ld+json">\n{json.dumps(faq_json, indent=2)}\n</script>'
    
    if '<script type="application/ld+json">' in content:
        # Insert after existing ld+json
        content = content.replace(
            '</script>\n</head>',
            '</script>\n' + schema_script + '\n</head>'
        )
    else:
        # Insert before </head>
        content = content.replace('</head>', schema_script + '\n</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  [ADDED] FAQ Schema with {len(data['questions'])} questions")
    return True

def main():
    print("=" * 60)
    print("Adding FAQ JSON-LD Schema to Calculator Pages")
    print("=" * 60)
    
    modified = []
    for filename, data in FAQ_SCHEMA_DATA.items():
        filepath = os.path.join(SITE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"\n[SKIP] {filename} - file not found")
            continue
        
        print(f"\nProcessing: {filename}")
        if add_faq_schema(filepath, data):
            modified.append(filename)
    
    print("\n" + "=" * 60)
    print(f"Done! Modified {len(modified)} files")
    for f in modified:
        print(f"  - {f}")
    print("=" * 60)

if __name__ == "__main__":
    main()

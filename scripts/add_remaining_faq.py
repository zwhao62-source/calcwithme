# -*- coding: utf-8 -*-
import os
import json
import re

SITE_DIR = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"

FAQ_DATA = {
    "parking-cost-calculator.html": {
        "questions": [
            {"q": "How much should I budget for parking?", "a": "Parking costs vary widely by location. Small cities: $40-80/month, medium cities: $100-150/month, large metros: $175-250/month, and premium downtown areas: $300-500+/month. Use our calculator to estimate your specific situation."},
            {"q": "Is a monthly parking pass worth it?", "a": "Yes, in most cases. Monthly passes typically offer 20-40% savings compared to daily rates. If you park in the same location regularly, a monthly pass almost always saves money and eliminates the hassle of daily payment."},
            {"q": "How do I calculate my annual parking costs?", "a": "Multiply your average daily parking rate by your work days per week, then by 52 weeks. Add any monthly passes, event parking, and weekend expenses. Our calculator does this automatically for you."},
            {"q": "What is the average parking cost in major US cities?", "a": "As of 2026, average monthly parking costs: New York ($500+), San Francisco ($400), Boston ($350), Chicago ($300), Seattle ($250), Denver ($200), Austin ($175). Prices vary by neighborhood and type of parking."}
        ]
    },
    "total-car-cost-calculator.html": {
        "questions": [
            {"q": "What is the true cost of owning a car?", "a": "Beyond the purchase price, true car costs include loan payments, gas, insurance, maintenance, repairs, parking, registration, and depreciation. Most people underestimate these costs by 30-50%. A $35,000 car can cost $50,000+ over 5 years when all factors are included."},
            {"q": "How much does depreciation affect car ownership cost?", "a": "Depreciation is often the largest hidden cost. A new car loses 20-30% of its value in the first year alone. Over 5 years, depreciation typically accounts for 40-50% of the total cost of ownership for a new vehicle."},
            {"q": "What is a reasonable cost per mile for car ownership?", "a": "A reasonable range is $0.50-1.00 per mile for a moderately-priced vehicle. This includes loan payments, gas, insurance, maintenance, and depreciation. Electric vehicles may have lower fuel and maintenance costs but similar depreciation."},
            {"q": "How often should I budget for major car maintenance?", "a": "Budget approximately $0.05-0.10 per mile for maintenance and repairs. This covers oil changes, tires, brakes, and unexpected repairs. Major expenses like transmission or engine work typically occur after 100,000+ miles."}
        ]
    },
    "index.html": {
        "questions": [
            {"q": "What is CalcWithMe?", "a": "CalcWithMe is a free online financial calculator platform offering 15+ tools for mortgage calculations, loan planning, investment growth, retirement planning, and more. All calculators are completely free to use with no sign-up required."},
            {"q": "Are CalcWithMe calculators accurate?", "a": "Yes. Our calculators use standard financial formulas and are regularly updated with current market rates. Results are for estimation purposes - for precise financial decisions, consult a licensed financial advisor."},
            {"q": "Is CalcWithMe free to use?", "a": "Yes, all calculators on CalcWithMe are completely free. We do not require registration, charge fees, or sell your data. Our calculators are funded by non-intrusive advertisements."},
            {"q": "How often are mortgage rates updated?", "a": "State-specific mortgage rates on our calculator are updated monthly based on market data. The default rates reflect average 30-year fixed mortgage rates for each US state and Canadian province."}
        ]
    }
}

def add_faq_schema_and_html(filepath, data):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Skip if already has FAQ schema
    if '"FAQPage"' in content:
        print(f"  [SKIP] Already has FAQ schema")
        return False
    
    # Build JSON-LD
    faq_json = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": item["q"],
             "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in data["questions"]
        ]
    }
    schema_script = '<script type="application/ld+json">\n' + json.dumps(faq_json, indent=2) + '\n</script>'
    
    # Add FAQ schema before </head>
    content = content.replace('</head>', schema_script + '\n</head>')
    
    # Add FAQ HTML before </div> closing calc-content or related-calcs
    faq_html = '''
                        <div class="faq-section">
                            <h3>Frequently Asked Questions</h3>
                            <details class="faq-item">
                                <summary>''' + data["questions"][0]["q"] + '''</summary>
                                <p>''' + data["questions"][0]["a"] + '''</p>
                            </details>
                            <details class="faq-item">
                                <summary>''' + data["questions"][1]["q"] + '''</summary>
                                <p>''' + data["questions"][1]["a"] + '''</p>
                            </details>
                            <details class="faq-item">
                                <summary>''' + data["questions"][2]["q"] + '''</summary>
                                <p>''' + data["questions"][2]["a"] + '''</p>
                            </details>
                            <details class="faq-item">
                                <summary>''' + data["questions"][3]["q"] + '''</summary>
                                <p>''' + data["questions"][3]["a"] + '''</p>
                            </details>
                        </div>
'''
    
    # Insert before related-calcs div or before closing main div
    if '<div class="related-calcs">' in content:
        content = content.replace('<div class="related-calcs">', faq_html + '\n                        <div class="related-calcs">')
    else:
        # Insert before </div> that closes calc-content
        content = content.replace('</div>\n                    </div>\n                </div>', faq_html + '\n                    </div>\n                </div>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  [DONE] FAQ Schema + HTML added")
    return True

print("=" * 60)
print("Adding FAQ to remaining pages")
print("=" * 60)

modified = []
for filename, data in FAQ_DATA.items():
    filepath = os.path.join(SITE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"\n[SKIP] {filename} - not found")
        continue
    print(f"\n{filename}")
    if add_faq_schema_and_html(filepath, data):
        modified.append(filename)

print("\n" + "=" * 60)
print(f"Done! Modified {len(modified)} files")
print("=" * 60)

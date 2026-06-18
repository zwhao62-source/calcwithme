import os

SITE_DIR = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"

def w(p, c):
    with open(p, "w", encoding="utf-8") as f:
        f.write(c)
    print(os.path.basename(p), len(c), "bytes")

HEAD = '<!DOCTYPE html>\n<html lang="en">\n<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
FOOT = '</main>\n<footer><div class="container"><div class="footer-bottom"><p>&copy; 2026 CalcWithMe.com. All rights reserved.</p><p class="disclaimer">Results are estimates only.</p></div></div></footer>\n</body></html>'
NAV = '<header><div class="container header-inner"><a href="/" class="logo"><span class="logo-icon">&#x1F522;</span><span>Calc<span class="highlight">With</span>Me</span></a><nav><a href="/">Calculators</a><a href="/blog/">Blog</a></nav></div></header>'

# ===== STUDENT LOAN CALCULATOR =====
w(os.path.join(SITE_DIR, "student-loan-calculator.html"), HEAD + """
<title>Student Loan Calculator - Free 2026 Repayment Estimator | CalcWithMe</title>
<meta name="description" content="Free student loan calculator. Estimate monthly payments, total interest, and payoff date for standard, graduated, and income-driven repayment plans.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/student-loan-calculator.html">
<link rel="stylesheet" href="css/style.css">
<meta property="og:title" content="Student Loan Calculator - CalcWithMe">
<script defer src="https://cloud.umami.is/script.js" data-website-id="77de646f-0376-43ee-8b45-326250fd1485"></script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://calcwithme.com"},{"@type":"ListItem","position":2,"name":"Financial","item":"https://calcwithme.com/#financial-calculators"},{"@type":"ListItem","position":3,"name":"Student Loan Calculator","item":"https://calcwithme.com/student-loan-calculator.html"}]}</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How much will I pay on a $30,000 student loan?","acceptedAnswer":{"@type":"Answer","text":"On the standard 10-year plan at 5.5%, monthly payment is about $327 and total paid is $39,220."}},{"@type":"Question","name":"What is the SAVE plan?","acceptedAnswer":{"@type":"Answer","text":"SAVE caps payments at 5% of discretionary income for undergrad loans and forgives remaining balance after 10-25 years."}}]}</script>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Student Loan Calculator</h1>
<p class="page-desc">Estimate monthly payments, total interest, and payoff date. Compare Standard, Graduated, and Extended repayment plans.</p>
<div class="calc-form">
<div class="form-group"><label>Total Loan Balance ($)</label><input type="number" id="loanBalance" value="37000" min="0" step="1000"></div>
<div class="form-row">
<div class="form-group"><label>Interest Rate (%)</label><input type="number" id="interestRate" value="5.5" min="0" max="20" step="0.1"></div>
<div class="form-group"><label>Repayment Plan</label><select id="repayPlan"><option value="standard">Standard (10 years)</option><option value="graduated">Graduated (10 years)</option><option value="extended">Extended (25 years)</option></select></div>
</div>
<div class="form-group"><label>Extra Monthly Payment ($)</label><input type="number" id="extraPayment" value="0" min="0" step="50"></div>
<button class="btn-calculate" onclick="calcStudentLoan()">Calculate Student Loan Payment</button>
</div>
<div class="calc-content">
<h2>How Student Loan Repayment Works</h2>
<p>Student loans accrue interest daily: Daily Interest = Balance x (Rate / 365.25). On $37,000 at 5.5%, that is $5.58/day.</p>
<h2>Standard vs Graduated vs Extended</h2>
<ul><li><strong>Standard (10yr)</strong>: Fixed payment, lowest total interest</li><li><strong>Graduated (10yr)</strong>: Starts low, increases every 2 years</li><li><strong>Extended (25yr)</strong>: Lower monthly but much more interest</li></ul>
<h2>The SAVE Plan (Income-Driven)</h2>
<p>SAVE caps payments at 5% of discretionary income for undergraduate loans. Remaining balance forgiven after 10-25 years. Government subsidizes unpaid interest.</p>
<h2>Extra Payments Save Thousands</h2>
<p>Adding $50/month extra on $37,000 at 5.5% saves over $4,000 in interest and shortens payoff by 2+ years.</p>
<h2>2026 Student Loan Rates</h2>
<ul><li>Direct Subsidized/Unsubsidized (Undergrad): ~5.50%</li><li>Direct Unsubsidized (Graduate): ~7.05%</li><li>Direct PLUS: ~8.05%</li><li>Private: 3.5%-15% depending on credit</li></ul>
</div></div>
<div class="results-panel"><h2>Results</h2>
<div class="result-item"><div class="result-label">Monthly Payment</div><div class="result-value" id="monthlyPayment">---</div></div>
<div class="result-item"><div class="result-label">Total Interest</div><div class="result-value secondary" id="totalInterest">---</div></div>
<div class="result-item"><div class="result-label">Total Paid</div><div class="result-value secondary" id="totalPaid">---</div></div>
<div class="result-item"><div class="result-label">Payoff Time</div><div class="result-value secondary" id="payoffTime">---</div></div>
<div class="result-item"><div class="result-label">Interest Savings</div><div class="result-value secondary" id="savings">---</div></div>
</div></div></div>""" + """
<script>
function fmt(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',')}
function calcStudentLoan(){
  const P=parseFloat(document.getElementById('loanBalance').value)||0;
  const r=(parseFloat(document.getElementById('interestRate').value)||0)/100/12;
  const plan=document.getElementById('repayPlan').value;
  const extra=parseFloat(document.getElementById('extraPayment').value)||0;
  let n=plan==='extended'?300:120;
  let monthly;if(r===0)monthly=P/n;else monthly=P*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1);
  let bal=P,mo=0,totalIntE=0,pm=monthly+extra;
  while(bal>0&&mo<600){let intr=bal*r;bal=bal+intr-pm;if(bal<0){totalIntE+=intr+bal;bal=0;}else totalIntE+=intr;mo++;}
  const baseInt=r===0?0:P*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1)*n-P;
  document.getElementById('monthlyPayment').textContent=fmt(monthly);
  document.getElementById('totalInterest').textContent=fmt(totalIntE);
  document.getElementById('totalPaid').textContent=fmt(P+totalIntE);
  document.getElementById('payoffTime').textContent=mo+' months ('+(mo/12).toFixed(1)+' yrs)';
  document.getElementById('savings').textContent=extra>0?fmt(baseInt-totalIntE):'$0';
}
calcStudentLoan();
</script>""" + FOOT)

# ===== SQUARE FOOTAGE CALCULATOR =====
w(os.path.join(SITE_DIR, "square-footage-calculator.html"), HEAD + """
<title>Square Footage Calculator - Free Area Calculator | CalcWithMe</title>
<meta name="description" content="Free square footage calculator. Calculate area for rectangles, circles, triangles, and trapezoids. Convert between sq ft, sq m, and acres.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/square-footage-calculator.html">
<link rel="stylesheet" href="css/style.css">
<script defer src="https://cloud.umami.is/script.js" data-website-id="77de646f-0376-43ee-8b45-326250fd1485"></script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How do I calculate square footage?","acceptedAnswer":{"@type":"Answer","text":"Multiply length by width. For a room 12ft x 15ft, the square footage is 180 sq ft."}},{"@type":"Question","name":"How many square feet in an acre?","acceptedAnswer":{"@type":"Answer","text":"One acre equals 43,560 square feet."}}]}</script>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Square Footage Calculator</h1>
<p class="page-desc">Calculate area in square feet, square meters, or acres. Perfect for flooring, painting, landscaping, and real estate.</p>
<div class="calc-form">
<div class="form-group"><label>Shape</label><select id="shape" onchange="updateShape()">
<option value="rectangle">Rectangle / Square</option><option value="circle">Circle</option>
<option value="triangle">Triangle</option><option value="trapezoid">Trapezoid</option></select></div>
<div id="shapeInputs"><div class="form-row"><div class="form-group"><label>Length (ft)</label><input type="number" id="length" value="12" min="0" step="0.1"></div><div class="form-group"><label>Width (ft)</label><input type="number" id="width" value="15" min="0" step="0.1"></div></div></div>
<div class="form-group"><label>Number of Same Areas</label><input type="number" id="count" value="1" min="1" step="1"></div>
<button class="btn-calculate" onclick="calcSqft()">Calculate Square Footage</button>
</div>
<div class="calc-content">
<h2>How to Calculate Square Footage</h2>
<p>Rectangle: Length x Width. Circle: pi x r2. Triangle: 0.5 x base x height. Trapezoid: 0.5 x (top + bottom) x height.</p>
<h2>Common Conversions</h2>
<ul><li>1 sq ft = 0.0929 sq m | 1 sq m = 10.764 sq ft</li><li>1 acre = 43,560 sq ft | 1 acre = 4,047 sq m</li></ul>
<h2>Cost by Square Foot</h2>
<ul><li>Hardwood flooring: $8-15/sq ft | Carpet: $3-7/sq ft | Tile: $10-25/sq ft</li><li>Interior paint: $2-6/sq ft (walls) | Sod: $0.30-0.80/sq ft</li></ul>
<h2>Measuring Irregular Shapes</h2>
<p>Break the area into simple shapes, calculate each, then add together. For an L-shaped room, split into two rectangles.</p>
</div></div>
<div class="results-panel"><h2>Area Results</h2>
<div class="result-item"><div class="result-label">Square Feet</div><div class="result-value" id="sqftResult">---</div></div>
<div class="result-item"><div class="result-label">Square Meters</div><div class="result-value secondary" id="sqmResult">---</div></div>
<div class="result-item"><div class="result-label">Acres</div><div class="result-value secondary" id="acresResult">---</div></div>
</div></div></div>""" + """
<script>
function updateShape(){
  const s=document.getElementById('shape').value,div=document.getElementById('shapeInputs');
  if(s==='rectangle')div.innerHTML='<div class="form-row"><div class="form-group"><label>Length (ft)</label><input type="number" id="length" value="12" min="0" step="0.1"></div><div class="form-group"><label>Width (ft)</label><input type="number" id="width" value="15" min="0" step="0.1"></div></div>';
  else if(s==='circle')div.innerHTML='<div class="form-group"><label>Radius (ft)</label><input type="number" id="radius" value="10" min="0" step="0.1"></div>';
  else if(s==='triangle')div.innerHTML='<div class="form-row"><div class="form-group"><label>Base (ft)</label><input type="number" id="base" value="10" min="0" step="0.1"></div><div class="form-group"><label>Height (ft)</label><input type="number" id="height" value="8" min="0" step="0.1"></div></div>';
  else if(s==='trapezoid')div.innerHTML='<div class="form-row"><div class="form-group"><label>Top Width (ft)</label><input type="number" id="topW" value="6" min="0" step="0.1"></div><div class="form-group"><label>Bottom Width (ft)</label><input type="number" id="botW" value="10" min="0" step="0.1"></div></div><div class="form-group"><label>Height (ft)</label><input type="number" id="trapH" value="8" min="0" step="0.1"></div>';
}
function calcSqft(){
  const s=document.getElementById('shape').value,c=parseInt(document.getElementById('count').value)||1;
  let area=0;
  if(s==='rectangle'){const l=parseFloat(document.getElementById('length').value)||0,w=parseFloat(document.getElementById('width').value)||0;area=l*w;}
  else if(s==='circle'){const r=parseFloat(document.getElementById('radius').value)||0;area=Math.PI*r*r;}
  else if(s==='triangle'){const b=parseFloat(document.getElementById('base').value)||0,h=parseFloat(document.getElementById('height').value)||0;area=0.5*b*h;}
  else if(s==='trapezoid'){const t=parseFloat(document.getElementById('topW').value)||0,b=parseFloat(document.getElementById('botW').value)||0,h=parseFloat(document.getElementById('trapH').value)||0;area=0.5*(t+b)*h;}
  area*=c;
  document.getElementById('sqftResult').textContent=area.toFixed(2)+' sq ft';
  document.getElementById('sqmResult').textContent=(area*0.0929).toFixed(2)+' sq m';
  document.getElementById('acresResult').textContent=(area/43560<1?(area/43560).toFixed(4):(area/43560).toFixed(2))+' acres';
}
calcSqft();
</script>""" + FOOT)

# ===== GRADE CALCULATOR =====
w(os.path.join(SITE_DIR, "grade-calculator.html"), HEAD + """
<title>Grade Calculator - Free Test & GPA Calculator 2026 | CalcWithMe</title>
<meta name="description" content="Free grade calculator. Calculate weighted averages, GPA, and what you need on the final exam to pass.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/grade-calculator.html">
<link rel="stylesheet" href="css/style.css">
<script defer src="https://cloud.umami.is/script.js" data-website-id="77de646f-0376-43ee-8b45-326250fd1485"></script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How do I calculate my class grade?","acceptedAnswer":{"@type":"Answer","text":"Multiply each category score by its weight, then add all weighted scores together."}},{"@type":"Question","name":"What do I need on the final?","acceptedAnswer":{"@type":"Answer","text":"Required Final = (Target - Current Weighted) / (1 - Final Weight)."}}]}</script>
<style>.grade-row{display:flex;gap:8px;align-items:center;margin-bottom:8px;padding:8px;background:#f8fafc;border-radius:8px;}.grade-row input{flex:1;min-width:50px;}.add-btn{background:#10b981;color:white;border:none;padding:8px 16px;border-radius:8px;cursor:pointer;font-weight:600;}.remove-btn{background:#ef4444;color:white;border:none;padding:4px 8px;border-radius:6px;cursor:pointer;font-size:.8rem;}</style>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Grade Calculator</h1>
<p class="page-desc">Calculate your class grade with weighted categories, find what you need on the final, or compute your GPA.</p>
<div class="calc-form">
<div id="gradeRows">
<div class="grade-row"><input type="text" value="Homework" class="gn"><input type="number" value="90" min="0" max="100" class="gs" placeholder="Grade %"><input type="number" value="30" min="0" max="100" class="gw" placeholder="Weight %"><button class="remove-btn" onclick="this.parentElement.remove();calcGrade()">X</button></div>
<div class="grade-row"><input type="text" value="Midterm" class="gn"><input type="number" value="85" min="0" max="100" class="gs" placeholder="Grade %"><input type="number" value="30" min="0" max="100" class="gw" placeholder="Weight %"><button class="remove-btn" onclick="this.parentElement.remove();calcGrade()">X</button></div>
<div class="grade-row"><input type="text" value="Final" class="gn"><input type="number" value="0" min="0" max="100" class="gs" placeholder="Grade %"><input type="number" value="40" min="0" max="100" class="gw" placeholder="Weight %"></div>
</div>
<button class="add-btn" onclick="addRow()">+ Add Category</button>
<div class="form-group" style="margin-top:16px;"><label>Target Grade (%)</label><input type="number" id="targetGrade" value="80" min="0" max="100"></div>
<button class="btn-calculate" onclick="calcGrade()">Calculate Grade</button>
</div>
<div class="calc-content">
<h2>How to Calculate Your Grade</h2>
<p>Multiply each category score by its weight: <strong>Overall = Sum(Grade x Weight)</strong>. For a class with Homework 90% (30%), Midterm 85% (30%), Final unknown (40%): current = 52.5% out of 60% weighted.</p>
<h2>What Do I Need on the Final?</h2>
<p><strong>Required = (Target - Current Weighted) / (1 - Final Weight)</strong>. To get 80% with 52.5% earned and final worth 40%: (80 - 52.5) / 0.40 = 68.75%. You need 69% on the final.</p>
<h2>GPA Scale</h2>
<ul><li>A+ (97-100): 4.0 | A (93-96): 4.0 | A- (90-92): 3.7</li><li>B+ (87-89): 3.3 | B (83-86): 3.0 | B- (80-82): 2.7</li><li>C+ (77-79): 2.3 | C (73-76): 2.0 | C- (70-72): 1.7</li><li>D (60-69): 1.0 | F (below 60): 0.0</li></ul>
</div></div>
<div class="results-panel"><h2>Grade Results</h2>
<div class="result-item"><div class="result-label">Current Weighted Grade</div><div class="result-value" id="currentGrade">---</div></div>
<div class="result-item"><div class="result-label">Total Weight</div><div class="result-value secondary" id="totalWeight">---</div></div>
<div class="result-item"><div class="result-label">Needed on Remaining</div><div class="result-value secondary" id="neededGrade">---</div></div>
<div class="result-item"><div class="result-label">Letter Grade</div><div class="result-value secondary" id="letterGrade">---</div></div>
</div></div></div>""" + """
<script>
function addRow(){const d=document.createElement('div');d.className='grade-row';d.innerHTML='<input type="text" value="Category" class="gn"><input type="number" value="0" min="0" max="100" class="gs" placeholder="Grade %"><input type="number" value="10" min="0" max="100" class="gw" placeholder="Weight %"><button class="remove-btn" onclick="this.parentElement.remove();calcGrade()">X</button>';document.getElementById('gradeRows').appendChild(d);}
function lg(p){if(p>=97)return'A+';if(p>=93)return'A';if(p>=90)return'A-';if(p>=87)return'B+';if(p>=83)return'B';if(p>=80)return'B-';if(p>=77)return'C+';if(p>=73)return'C';if(p>=70)return'C-';if(p>=60)return'D';return'F';}
function calcGrade(){
  const rows=document.querySelectorAll('.grade-row');let sum=0,ws=0;
  rows.forEach(r=>{const s=parseFloat(r.querySelector('.gs').value)||0;const w=parseFloat(r.querySelector('.gw').value)||0;sum+=s*w/100;ws+=w;});
  const target=parseFloat(document.getElementById('targetGrade').value)||80;
  const needed=ws<100?((target-sum)/(100-ws)*100):0;
  document.getElementById('currentGrade').textContent=(ws>0?sum/(ws/100):0).toFixed(2)+'%';
  document.getElementById('totalWeight').textContent=ws.toFixed(1)+'%';
  document.getElementById('neededGrade').textContent=ws<100?needed.toFixed(2)+'%':'All weight entered';
  document.getElementById('letterGrade').textContent=lg(ws>0?sum/(ws/100):0);
}
calcGrade();
</script>""" + FOOT)

# ===== OVERTIME CALCULATOR =====
w(os.path.join(SITE_DIR, "overtime-calculator.html"), HEAD + """
<title>Overtime Calculator - Free 2026 OT Pay Estimator | CalcWithMe</title>
<meta name="description" content="Free overtime calculator. Calculate overtime pay at 1.5x, double time. Federal and state OT rules included.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/overtime-calculator.html">
<link rel="stylesheet" href="css/style.css">
<script defer src="https://cloud.umami.is/script.js" data-website-id="77de646f-0376-43ee-8b45-326250fd1485"></script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How is overtime calculated?","acceptedAnswer":{"@type":"Answer","text":"Federal law requires 1.5x pay for hours over 40 per week. Some states have daily overtime rules."}},{"@type":"Question","name":"What is time-and-a-half?","acceptedAnswer":{"@type":"Answer","text":"1.5 times your regular hourly rate. At $20/hr, OT is $30/hr."}}]}</script>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Overtime Calculator</h1>
<p class="page-desc">Calculate overtime pay including time-and-a-half (1.5x) and double time (2x).</p>
<div class="calc-form">
<div class="form-row"><div class="form-group"><label>Hourly Rate ($)</label><input type="number" id="hourlyRate" value="20" min="0" step="0.5"></div><div class="form-group"><label>Regular Hours/Week</label><input type="number" id="regularHours" value="40" min="0" max="40"></div></div>
<div class="form-row"><div class="form-group"><label>Overtime Hours (1.5x)</label><input type="number" id="ot15" value="5" min="0"></div><div class="form-group"><label>Double Time Hours (2x)</label><input type="number" id="ot2x" value="0" min="0"></div></div>
<button class="btn-calculate" onclick="calcOT()">Calculate Overtime Pay</button>
</div>
<div class="calc-content">
<h2>How Overtime Pay Works</h2>
<p>FLSA requires <strong>1.5x pay</strong> for hours over 40/week. At $20/hr regular, OT is $30/hr.</p>
<h2>State Overtime Rules</h2>
<ul><li><strong>California</strong>: 1.5x for 8-12 hrs/day, 2x for 12+ hrs/day</li><li><strong>Alaska</strong>: 1.5x for hours over 8/day or 40/week</li><li><strong>Nevada</strong>: 1.5x for hours over 8/day (if earning less than 1.5x minimum wage)</li><li><strong>Colorado</strong>: 1.5x for hours over 12/day or 40/week</li></ul>
<h2>Exempt vs Non-Exempt</h2>
<p>Employees earning above $43,888/year (2026) in executive/administrative/professional roles are generally exempt from OT.</p>
<h2>Overtime Formula</h2>
<p><strong>Total = Regular Hours x Rate + OT Hours x (Rate x 1.5) + Double Time x (Rate x 2)</strong></p>
<p>Example: 40 hrs at $20 + 5 hrs at $30 = $800 + $150 = $950/week</p>
</div></div>
<div class="results-panel"><h2>Pay Results</h2>
<div class="result-item"><div class="result-label">Regular Pay</div><div class="result-value" id="regularPay">---</div></div>
<div class="result-item"><div class="result-label">Overtime Pay (1.5x)</div><div class="result-value secondary" id="otPay15">---</div></div>
<div class="result-item"><div class="result-label">Double Time (2x)</div><div class="result-value secondary" id="otPay2x">---</div></div>
<div class="result-item"><div class="result-label">Total Weekly Pay</div><div class="result-value" id="totalPay">---</div></div>
<div class="result-item"><div class="result-label">Effective Hourly Rate</div><div class="result-value secondary" id="effectiveRate">---</div></div>
</div></div></div>""" + """
<script>
function fmt(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',')}
function calcOT(){
  const rate=parseFloat(document.getElementById('hourlyRate').value)||0;
  const rh=parseFloat(document.getElementById('regularHours').value)||0;
  const ot1=parseFloat(document.getElementById('ot15').value)||0;
  const ot2=parseFloat(document.getElementById('ot2x').value)||0;
  const reg=rate*rh,ot15p=rate*1.5*ot1,ot2p=rate*2*ot2,total=reg+ot15p+ot2p;
  const th=rh+ot1+ot2;
  document.getElementById('regularPay').textContent=fmt(reg);
  document.getElementById('otPay15').textContent=fmt(ot15p);
  document.getElementById('otPay2x').textContent=fmt(ot2p);
  document.getElementById('totalPay').textContent=fmt(total);
  document.getElementById('effectiveRate').textContent=th>0?fmt(total/th)+'/hr':'$0';
}
calcOT();
</script>""" + FOOT)

# ===== HOURS CALCULATOR =====
w(os.path.join(SITE_DIR, "hours-calculator.html"), HEAD + """
<title>Hours Calculator - Free Time Duration Calculator | CalcWithMe</title>
<meta name="description" content="Free hours calculator. Calculate hours between two times, total work hours, and time duration.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/hours-calculator.html">
<link rel="stylesheet" href="css/style.css">
<script defer src="https://cloud.umami.is/script.js" data-website-id="77de646f-0376-43ee-8b45-326250fd1485"></script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How do I calculate hours between two times?","acceptedAnswer":{"@type":"Answer","text":"Subtract start time from end time. From 9 AM to 5 PM is 8 hours."}},{"@type":"Question","name":"How many hours is 8:30 AM to 5:45 PM?","acceptedAnswer":{"@type":"Answer","text":"9 hours 15 minutes, or 9.25 hours."}}]}</script>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Hours Calculator</h1>
<p class="page-desc">Calculate hours and minutes between two times, total work hours, and time duration.</p>
<div class="calc-form">
<div class="form-row"><div class="form-group"><label>Start Time</label><input type="time" id="startTime" value="09:00"></div><div class="form-group"><label>End Time</label><input type="time" id="endTime" value="17:00"></div></div>
<div class="form-group"><label>Lunch Break (minutes)</label><input type="number" id="lunch" value="30" min="0" step="15"></div>
<button class="btn-calculate" onclick="calcHours()">Calculate Hours</button>
</div>
<div class="calc-content">
<h2>How to Calculate Hours Between Times</h2>
<p>Convert to 24-hour format, subtract start from end. If end is earlier, add 24 hours (crossing midnight). Then subtract break time.</p>
<h2>Time Math Tips</h2>
<ul><li>15 min = 0.25 hrs | 30 min = 0.5 hrs | 45 min = 0.75 hrs</li><li>For payroll, round to nearest quarter hour</li><li>Cross-midnight: 10 PM to 6 AM = 8 hours</li></ul>
<h2>Common Work Hours</h2>
<ul><li>9 AM to 5 PM = 8 hours | 8:30 AM to 5:30 PM = 9 hours</li><li>7 AM to 3:30 PM = 8.5 hours | 11 PM to 7 AM = 8 hours (overnight)</li></ul>
</div></div>
<div class="results-panel"><h2>Time Results</h2>
<div class="result-item"><div class="result-label">Total Hours</div><div class="result-value" id="totalHours">---</div></div>
<div class="result-item"><div class="result-label">Decimal Hours</div><div class="result-value secondary" id="decimalHours">---</div></div>
<div class="result-item"><div class="result-label">After Break</div><div class="result-value secondary" id="afterLunch">---</div></div>
<div class="result-item"><div class="result-label">Weekly (x5)</div><div class="result-value secondary" id="weekly">---</div></div>
</div></div></div>""" + """
<script>
function calcHours(){
  const s=document.getElementById('startTime').value.split(':');
  const e=document.getElementById('endTime').value.split(':');
  const lunch=parseInt(document.getElementById('lunch').value)||0;
  let start=parseInt(s[0])*60+parseInt(s[1]),end=parseInt(e[0])*60+parseInt(e[1]);
  if(end<=start)end+=24*60;
  const totalM=end-start,afterM=totalM-lunch;
  document.getElementById('totalHours').textContent=Math.floor(totalM/60)+' hrs '+totalM%60+' min';
  document.getElementById('decimalHours').textContent=(totalM/60).toFixed(2)+' hrs';
  document.getElementById('afterLunch').textContent=Math.floor(afterM/60)+' hrs '+afterM%60+' min ('+(afterM/60).toFixed(2)+' hrs)';
  document.getElementById('weekly').textContent=(afterM/60*5).toFixed(1)+' hrs/week';
}
calcHours();
</script>""" + FOOT)

print("All 5 new calculators created!")

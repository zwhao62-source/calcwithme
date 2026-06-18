import os

SITE_DIR = r"C:\Users\Administrator\.qclaw\workspace\calcwithme-site"

def w(p, c):
    with open(p, "w", encoding="utf-8") as f:
        f.write(c)
    print(os.path.basename(p), len(c), "bytes")

NAV = '<header><div class="container header-inner"><a href="/" class="logo"><span class="logo-icon">&#x1F522;</span><span>Calc<span class="highlight">With</span>Me</span></a><nav><a href="/">Calculators</a><a href="/blog/">Blog</a></nav></div></header>'
HEAD = '<!DOCTYPE html>\n<html lang="en">\n<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">\n<link rel="stylesheet" href="css/style.css">\n<script defer src="https://cloud.umami.is/script.js" data-website-id="77de646f-0376-43ee-8b45-326250fd1485"></script>\n'
FOOT = '</main>\n<footer><div class="container"><div class="footer-bottom"><p>&copy; 2026 CalcWithMe.com. All rights reserved.</p></div></div></footer>\n</body></html>'

# ── BODY FAT CALCULATOR ──
w(os.path.join(SITE_DIR,"body-fat-calculator.html"), HEAD + """
<title>Body Fat Calculator - Free US Navy Method Calculator 2026 | CalcWithMe</title>
<meta name="description" content="Free body fat calculator using the US Navy method. Enter your measurements to estimate body fat percentage for men and women.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/body-fat-calculator.html">
<meta property="og:title" content="Body Fat Calculator - CalcWithMe">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://calcwithme.com"},{"@type":"ListItem","position":2,"name":"Health","item":"https://calcwithme.com/#health-fitness"},{"@type":"ListItem","position":3,"name":"Body Fat Calculator","item":"https://calcwithme.com/body-fat-calculator.html"}]}</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How is body fat percentage calculated?","acceptedAnswer":{"@type":"Answer","text":"The US Navy method uses circumference measurements of neck, waist, and hips to estimate body fat. For women, hip measurement is also included."}},{"@type":"Question","name":"What is a healthy body fat percentage?","acceptedAnswer":{"@type":"Answer","text":"Essential fat: men 2-5%, women 10-13%. Athletes: men 6-13%, women 14-20%. Fitness: men 14-17%, women 21-24%. Average: men 18-24%, women 25-31%."}}]}</script>
<style>.bf-result{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:20px;}.bf-bar{height:20px;border-radius:10px;background:#e2e8f0;overflow:hidden;margin:8px 0;}.bf-fill{height:100%;border-radius:10px;transition:width 0.5s;}</style>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Body Fat Calculator</h1>
<p class="page-desc">Estimate your body fat percentage using the US Navy method. Enter your measurements for an accurate estimate.</p>
<div class="calc-form">
<div class="form-group"><label>Sex</label><select id="sex" onchange="toggleSex()"><option value="male">Male</option><option value="female">Female</option></select></div>
<div class="form-row">
<div class="form-group"><label>Height (inches)</label><input type="number" id="height" value="70" min="48" max="96" step="0.5"></div>
<div class="form-group"><label>Weight (lbs)</label><input type="number" id="weight" value="180" min="50" max="500" step="1"></div>
</div>
<div class="form-group"><label>Neck Circumference (inches)</label><input type="number" id="neck" value="15" min="5" max="30" step="0.1"></div>
<div class="form-group"><label>Waist Circumference (inches)</label><input type="number" id="waist" value="34" min="10" max="80" step="0.1"><div class="help-text">Measure at navel level</div></div>
<div class="form-group" id="hipGroup" style="display:none;"><label>Hip Circumference (inches)</label><input type="number" id="hip" value="38" min="10" max="80" step="0.1"><div class="help-text">Measure at the widest point</div></div>
<button class="btn-calculate" onclick="calcBF()">Calculate Body Fat</button>
</div>
<div class="calc-content">
<h2>How the US Navy Body Fat Formula Works</h2>
<p><strong>Men:</strong> Body Fat % = 86.010 x log10(waist - neck) - 70.041 x log10(height) + 36.76</p>
<p><strong>Women:</strong> Body Fat % = 163.205 x log10(waist + hip - neck) - 97.684 x log10(height) - 78.387</p>
<h2>Body Fat Categories</h2>
<table class="schedule-table"><thead><tr><th>Category</th><th>Men</th><th>Women</th></tr></thead><tbody>
<tr><td>Essential Fat</td><td>2-5%</td><td>10-13%</td></tr>
<tr><td>Athletes</td><td>6-13%</td><td>14-20%</td></tr>
<tr><td>Fitness</td><td>14-17%</td><td>21-24%</td></tr>
<tr><td>Average</td><td>18-24%</td><td>25-31%</td></tr>
<tr><td>Obese</td><td>&gt;25%</td><td>&gt;32%</td></tr>
</tbody></table>
<h2>Other Methods to Measure Body Fat</h2>
<ul><li><strong>Skinfold calipers</strong>: Pinch skin at specific sites, ~3-4% accuracy</li><li><strong>Bioelectrical impedance</strong>: Scales send current through body, ~3% error</li><li><strong>DEXA scan</strong>: X-ray based, most accurate at ~1-2% error</li><li><strong>Hydrostatic weighing</strong>: Gold standard, 1-2% accuracy</li></ul>
</div></div>
<div class="results-panel"><h2>Body Fat Results</h2>
<div class="result-item"><div class="result-label">Estimated Body Fat</div><div class="result-value" id="bfPct">---</div></div>
<div class="result-item"><div class="result-label">Category</div><div class="result-value secondary" id="bfCat">---</div></div>
<div class="result-item"><div class="result-label">Fat Mass (lbs)</div><div class="result-value secondary" id="bfMass">---</div></div>
<div class="result-item"><div class="result-label">Lean Mass (lbs)</div><div class="result-value secondary" id="leanMass">---</div></div>
<div class="bf-result">
<div id="bfBar" class="bf-bar"><div id="bfFill" class="bf-fill" style="width:0%"></div></div>
</div>
</div></div></div>""" + """
<script>
function toggleSex(){
  document.getElementById('hipGroup').style.display=document.getElementById('sex').value==='female'?'block':'none';
}
function calcBF(){
  const sex=document.getElementById('sex').value;
  const h=parseFloat(document.getElementById('height').value)||0;
  const w=parseFloat(document.getElementById('weight').value)||0;
  const n=parseFloat(document.getElementById('neck').value)||0;
  const waist=parseFloat(document.getElementById('waist').value)||0;
  let bf;
  if(sex==='male'){
    bf=86.010*Math.log10(waist-n)-70.041*Math.log10(h)+36.76;
  }else{
    const hip=parseFloat(document.getElementById('hip').value)||0;
    bf=163.205*Math.log10(waist+hip-n)-97.684*Math.log10(h)-78.387;
  }
  bf=Math.max(2,Math.min(60,bf));
  const fatMass=w*bf/100;
  const lean=w-fatMass;
  const cats=sex==='male'?[[2,'Essential'],[6,'Athletes'],[14,'Fitness'],[18,'Average'],[25,'Obese']]:[[10,'Essential'],[14,'Athletes'],[21,'Fitness'],[25,'Average'],[32,'Obese']];
  let cat='Obese';for(const [t,c] of cats)if(bf>=t)cat=c;
  const pct=Math.round(bf*10)/10;
  document.getElementById('bfPct').textContent=pct+'%';
  document.getElementById('bfCat').textContent=cat;
  document.getElementById('bfMass').textContent=fatMass.toFixed(1)+' lbs';
  document.getElementById('leanMass').textContent=lean.toFixed(1)+' lbs';
  const fill=document.getElementById('bfFill');
  const colors=['#ef4444','#f97316','#eab308','#22c55e'];
  const colorIdx=Math.min(3,Math.floor(pct/7));
  fill.style.width=Math.min(100,pct)+'%';
  fill.style.background=colors[colorIdx];
}
calcBF();
</script>""" + FOOT)

# ── BMR CALCULATOR ──
w(os.path.join(SITE_DIR,"bmr-calculator.html"), HEAD + """
<title>BMR Calculator - Basal Metabolic Rate Free Calculator 2026 | CalcWithMe</title>
<meta name="description" content="Free BMR calculator. Calculate your basal metabolic rate using Mifflin-St Jeor, Harris-Benedict, or Katch-McArdle formulas.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/bmr-calculator.html">
<meta property="og:title" content="BMR Calculator - CalcWithMe">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://calcwithme.com"},{"@type":"ListItem","position":2,"name":"Health","item":"https://calcwithme.com/#health-fitness"},{"@type":"ListItem","position":3,"name":"BMR Calculator","item":"https://calcwithme.com/bmr-calculator.html"}]}</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is BMR?","acceptedAnswer":{"@type":"Answer","text":"BMR (Basal Metabolic Rate) is the number of calories your body burns at rest just to maintain basic life functions like breathing, circulation, and cell production."}},{"@type":"Question","name":"How many calories should I eat to lose weight?","acceptedAnswer":{"@type":"Answer","text":"Multiply your BMR by an activity factor (1.2 for sedentary to 1.9 for very active) to get TDEE, then subtract 500 calories/day to lose ~1 lb/week."}}]}</script>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>BMR Calculator</h1>
<p class="page-desc">Calculate your Basal Metabolic Rate — the calories your body burns at rest. Use Mifflin-St Jeor (most accurate) or Harris-Benedict formula.</p>
<div class="calc-form">
<div class="form-group"><label>Formula</label><select id="formula"><option value="mifflin">Mifflin-St Jeor (Recommended)</option><option value="harris">Harris-Benedict</option></select></div>
<div class="form-group"><label>Sex</label><select id="sex"><option value="male">Male</option><option value="female">Female</option></select></div>
<div class="form-row">
<div class="form-group"><label>Age (years)</label><input type="number" id="age" value="30" min="15" max="100"></div>
<div class="form-group"><label>Height (inches)</label><input type="number" id="height" value="68" min="48" max="96"></div>
</div>
<div class="form-group"><label>Weight (lbs)</label><input type="number" id="weight" value="160" min="50" max="500"></div>
<div class="form-group"><label>Activity Level</label><select id="activity">
<option value="1.2">Sedentary (little or no exercise)</option>
<option value="1.375">Light (exercise 1-3 days/week)</option>
<option value="1.55" selected>Moderate (exercise 3-5 days/week)</option>
<option value="1.725">Active (exercise 6-7 days/week)</option>
<option value="1.9">Very Active (hard exercise daily)</option>
</select></div>
<button class="btn-calculate" onclick="calcBMR()">Calculate BMR</button>
</div>
<div class="calc-content">
<h2>What Is BMR?</h2>
<p>BMR is the number of calories your body burns at complete rest to maintain vital functions — breathing, circulation, cell production, brain function. It accounts for 60-75% of your total daily calorie burn.</p>
<h2>The Mifflin-St Jeor Equation (Most Accurate)</h2>
<p><strong>Men:</strong> BMR = 10 x weight(kg) + 6.25 x height(cm) - 5 x age + 5</p>
<p><strong>Women:</strong> BMR = 10 x weight(kg) + 6.25 x height(cm) - 5 x age - 161</p>
<h2>TDEE: Total Daily Energy Expenditure</h2>
<p>Multiply BMR by an activity multiplier to get TDEE:</p>
<ul><li>Sedentary (desk job): BMR x 1.2</li><li>Light activity: BMR x 1.375</li><li>Moderate activity (3-5x/week): BMR x 1.55</li><li>Very active: BMR x 1.725</li><li>Athletes: BMR x 1.9</li></ul>
<h2>How to Use BMR for Weight Goals</h2>
<ul><li>To lose 1 lb/week: TDEE - 500 calories/day</li><li>To gain 1 lb/week: TDEE + 500 calories/day</li><li>Never eat below 1200 cal/day (women) or 1500 cal/day (men)</li></ul>
</div></div>
<div class="results-panel"><h2>Your Results</h2>
<div class="result-item"><div class="result-label">BMR (at rest)</div><div class="result-value" id="bmrResult">---</div></div>
<div class="result-item"><div class="result-label">TDEE (with activity)</div><div class="result-value" id="tdeeResult">---</div></div>
<div class="result-item"><div class="result-label">Weight Loss (-500 cal)</div><div class="result-value secondary" id="cutResult">---</div></div>
<div class="result-item"><div class="result-label">Weight Gain (+500 cal)</div><div class="result-value secondary" id="bulkResult">---</div></div>
</div></div></div>""" + """
<script>
function calcBMR(){
  const sex=document.getElementById('sex').value;
  const age=parseFloat(document.getElementById('age').value)||0;
  const h=parseFloat(document.getElementById('height').value)*2.54||0; // inches to cm
  const w=parseFloat(document.getElementById('weight').value)*0.453592||0; // lbs to kg
  const act=parseFloat(document.getElementById('activity').value)||1.2;
  const formula=document.getElementById('formula').value;
  let bmr;
  if(formula==='mifflin'){
    bmr=sex==='male'?10*w+6.25*h-5*age+5:10*w+6.25*h-5*age-161;
  }else{
    bmr=sex==='male'?88.362+13.397*w+4.799*h-5.677*age:447.593+9.247*w+3.098*h-4.33*age;
  }
  const tdee=bmr*act;
  document.getElementById('bmrResult').textContent=Math.round(bmr)+' cal/day';
  document.getElementById('tdeeResult').textContent=Math.round(tdee)+' cal/day';
  document.getElementById('cutResult').textContent=Math.round(tdee-500)+' cal/day';
  document.getElementById('bulkResult').textContent=Math.round(tdee+500)+' cal/day';
}
calcBMR();
</script>""" + FOOT)

# ── IDEAL WEIGHT CALCULATOR ──
w(os.path.join(SITE_DIR,"ideal-weight-calculator.html"), HEAD + """
<title>Ideal Weight Calculator - Free Healthy Weight Estimator 2026 | CalcWithMe</title>
<meta name="description" content="Free ideal weight calculator. Find your healthy weight range using BMI, Devine, Robinson, and Miller formulas.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/ideal-weight-calculator.html">
<meta property="og:title" content="Ideal Weight Calculator - CalcWithMe">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is my ideal weight?","acceptedAnswer":{"@type":"Answer","text":"Your ideal weight depends on height, sex, and frame size. A BMI of 18.5-24.9 is considered healthy for most adults."}},{"@type":"Question","name":"What is the Robinson formula?","acceptedAnswer":{"@type":"Answer","text":"Men: 114 lb + 4 lb/inch over 5 ft. Women: 108 lb + 3.5 lb/inch over 5 ft. Adjusts by 10% for large or small frame."}}]}</script>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Ideal Weight Calculator</h1>
<p class="page-desc">Find your healthy weight range based on height. Uses BMI, Devine, Robinson, and Miller formulas.</p>
<div class="calc-form">
<div class="form-group"><label>Sex</label><select id="sex"><option value="male">Male</option><option value="female">Female</option></select></div>
<div class="form-group"><label>Height (inches)</label><input type="number" id="height" value="68" min="48" max="96"></div>
<div class="form-group"><label>Frame Size</label><select id="frame"><option value="0.9">Small Frame</option><option value="1" selected>Medium Frame</option><option value="1.1">Large Frame</option></select></div>
<button class="btn-calculate" onclick="calcIdeal()">Calculate Ideal Weight</button>
</div>
<div class="calc-content">
<h2>What Is Ideal Body Weight?</h2>
<p>Ideal body weight (IBW) is a weight estimate based on height that is associated with optimal health outcomes. It serves as a guideline rather than a precise target.</p>
<h2>Formulas Used</h2>
<ul><li><strong>BMI Range (18.5-24.9)</strong>: The CDC and WHO standard for healthy weight</li><li><strong>Devine Formula</strong>: Originally for dosing medications; 100 lb + 5 lb/inch over 5 ft</li><li><strong>Robinson Formula</strong>: Modified from Devine; considered more accurate for adults</li><li><strong>Miller Formula</strong>: Another commonly used estimate</li></ul>
<h2>Limitations of Ideal Weight Formulas</h2>
<p>These formulas were developed from limited population data and don't account for muscle mass, bone density, age, or body composition. Athletes with high muscle mass may exceed these ranges and still be healthy.</p>
<h2>Better Alternative</h2>
<p>Use BMI (18.5-24.9 healthy range) combined with waist circumference for a more complete picture. Waist over 40" (men) or 35" (women) indicates higher health risk regardless of weight.</p>
</div></div>
<div class="results-panel"><h2>Your Results</h2>
<div class="result-item"><div class="result-label">BMI Range (18.5-24.9)</div><div class="result-value" id="bmiRange">---</div></div>
<div class="result-item"><div class="result-label">Devine Formula</div><div class="result-value secondary" id="devine">---</div></div>
<div class="result-item"><div class="result-label">Robinson Formula</div><div class="result-value secondary" id="robinson">---</div></div>
<div class="result-item"><div class="result-label">Miller Formula</div><div class="result-value secondary" id="miller">---</div></div>
</div></div></div>""" + """
<script>
function calcIdeal(){
  const sex=document.getElementById('sex').value;
  const h=parseFloat(document.getElementById('height').value)||0;
  const frame=parseFloat(document.getElementById('frame').value)||1;
  const extra=h-60; // inches over 5 ft (60 inches)
  // BMI range
  const bmiLow=18.5*Math.pow(h*0.0254,2)/0.453592;
  const bmiHigh=24.9*Math.pow(h*0.0254,2)/0.453592;
  // Devine: 100+(5*extra) men, 95.5+(5*extra) women
  const devine=((sex==='male'?100:95.5)+5*extra)*frame;
  // Robinson: 114+(3*extra) men, 108+(3*extra) women
  const robinson=((sex==='male'?114:108)+3*extra)*frame;
  // Miller: 131+(2.7*extra) men, 123+(3*extra) women
  const miller=((sex==='male'?131:123)+(sex==='male'?2.7:3)*extra)*frame;
  document.getElementById('bmiRange').textContent=Math.round(bmiLow)+' - '+Math.round(bmiHigh)+' lbs';
  document.getElementById('devine').textContent=Math.round(devine)+' lbs';
  document.getElementById('robinson').textContent=Math.round(robinson)+' lbs';
  document.getElementById('miller').textContent=Math.round(miller)+' lbs';
}
calcIdeal();
</script>""" + FOOT)

# ── PREGNANCY CALCULATOR ──
w(os.path.join(SITE_DIR,"pregnancy-calculator.html"), HEAD + """
<title>Pregnancy Calculator - Due Date & Conception Date Calculator 2026 | CalcWithMe</title>
<meta name="description" content="Free pregnancy calculator. Enter your last period or conception date to find your due date, trimester milestones, and fetal development stages.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/pregnancy-calculator.html">
<meta property="og:title" content="Pregnancy Calculator - CalcWithMe">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How is my due date calculated?","acceptedAnswer":{"@type":"Answer","text":"Naegele's rule: Add 280 days (40 weeks) to the first day of your last menstrual period. This assumes a 28-day cycle with ovulation on day 14."}},{"@type":"Question","name":"How accurate is the due date?","acceptedAnswer":{"@type":"Answer","text":"Only about 4% of babies are born on their due date. Most arrive within 2 weeks before or after."}}]}</script>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Pregnancy Calculator</h1>
<p class="page-desc">Calculate your due date, current trimester, weeks pregnant, and key fetal development milestones.</p>
<div class="calc-form">
<div class="form-group"><label>First Day of Last Period</label><input type="date" id="lmp" value="2026-03-18"></div>
<div class="form-group"><label>Average Cycle Length (days)</label><select id="cycle">
<option value="21">21 days</option><option value="28" selected>28 days (average)</option>
<option value="30">30 days</option><option value="35">35 days</option>
</select></div>
<button class="btn-calculate" onclick="calcPreg()">Calculate Pregnancy Timeline</button>
</div>
<div class="calc-content">
<h2>How Pregnancy Is Calculated</h2>
<p>Pregnancy is measured from the first day of your last menstrual period (LMP). This is called the gestational age. Conception typically occurs about 14 days after LMP in a 28-day cycle.</p>
<h2>Key Pregnancy Milestones</h2>
<ul><li><strong>Week 4</strong>: Implantation occurs, pregnancy test turns positive</li><li><strong>Week 8</strong>: Heartbeat detectable on ultrasound</li><li><strong>Week 12</strong>: End of first trimester, miscarriage risk drops significantly</li><li><strong>Week 20</strong>: Anatomy scan, may reveal baby's sex</li><li><strong>Week 24</strong>: Viability milestone — baby has a chance of survival if born</li><li><strong>Week 37</strong>: Baby is considered full-term</li></ul>
<h2>The Three Trimesters</h2>
<ul><li><strong>First Trimester (Weeks 1-12)</strong>: Rapid cell division, organ formation. Most common for nausea and fatigue.</li><li><strong>Second Trimester (Weeks 13-26)</strong>: Growth phase. Most women feel best during this period. Baby movements felt ("quickening").</li><li><strong>Third Trimester (Weeks 27-40)</strong>: Rapid brain development, fat accumulation. Common discomforts: back pain, swelling, shortness of breath.</li></ul>
<h2>Important Notes</h2>
<p>Only ~4% of babies arrive on their due date. First-time moms often go past their due date; subsequent pregnancies tend to arrive sooner.</p>
</div></div>
<div class="results-panel"><h2>Your Pregnancy Timeline</h2>
<div class="result-item"><div class="result-label">Due Date</div><div class="result-value" id="dueDate">---</div></div>
<div class="result-item"><div class="result-label">Weeks Pregnant</div><div class="result-value" id="weeksPreg">---</div></div>
<div class="result-item"><div class="result-label">Current Trimester</div><div class="result-value secondary" id="trimester">---</div></div>
<div class="result-item"><div class="result-label">Conception Date</div><div class="result-value secondary" id="conception">---</div></div>
<div class="result-item"><div class="result-label">Days Until Due Date</div><div class="result-value secondary" id="daysLeft">---</div></div>
</div></div></div>""" + """
<script>
function calcPreg(){
  const lmp=new Date(document.getElementById('lmp').value);
  const cycle=parseInt(document.getElementById('cycle').value)||28;
  const ovulation=new Date(lmp.getTime()+(cycle-14)*86400000);
  const dueDate=new Date(lmp.getTime()+280*86400000);
  const today=new Date();
  const daysDiff=Math.floor((today-lmp)/86400000);
  const weeks=Math.floor(daysDiff/7);
  const daysRem=daysDiff%7;
  const tri=weeks<13?'First Trimester':weeks<27?'Second Trimester':'Third Trimester';
  const daysLeft=Math.max(0,Math.floor((dueDate-today)/86400000));
  const fmt=d=>d.toLocaleDateString('en-US',{weekday:'long',year:'numeric',month:'long',day:'numeric'});
  document.getElementById('dueDate').textContent=fmt(dueDate);
  document.getElementById('weeksPreg').textContent=weeks+' weeks, '+daysRem+' days';
  document.getElementById('trimester').textContent=tri;
  document.getElementById('conception').textContent=fmt(ovulation);
  document.getElementById('daysLeft').textContent=daysLeft+' days';
}
calcPreg();
</script>""" + FOOT)

# ── PACE CALCULATOR ──
w(os.path.join(SITE_DIR,"pace-calculator.html"), HEAD + """
<title>Pace Calculator - Running & Cycling Pace Calculator 2026 | CalcWithMe</title>
<meta name="description" content="Free pace calculator. Calculate your running or cycling pace, speed, and finish times for any distance from 5K to marathon.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/pace-calculator.html">
<meta property="og:title" content="Pace Calculator - CalcWithMe">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How do I calculate running pace?","acceptedAnswer":{"@type":"Answer","text":"Pace = Time / Distance. For example, running 5K in 25 minutes: 25/5 = 5 min/km or 8:03 min/mile."}},{"@type":"Question","name":"What is a good marathon pace?","acceptedAnswer":{"@type":"Answer","text":"A 4-hour marathon = 9:09 min/mile (5:41 min/km). A 3:30 marathon = 8:01 min/mile (4:59 min/km)."}}]}</script>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Pace Calculator</h1>
<p class="page-desc">Calculate your running or cycling pace, speed, and predicted finish times for any distance.</p>
<div class="calc-form">
<div class="form-group"><label>Calculate By</label><select id="calcBy" onchange="togglePace()"><option value="time">Time & Distance → Pace</option><option value="pace">Pace & Distance → Time</option></select></div>
<div class="form-row">
<div class="form-group"><label>Hours</label><input type="number" id="ph" value="0" min="0"></div>
<div class="form-group"><label>Minutes</label><input type="number" id="pm" value="30" min="0" max="59"></div>
<div class="form-group"><label>Seconds</label><input type="number" id="ps" value="0" min="0" max="59"></div>
</div>
<div class="form-group"><label>Distance</label><div style="display:flex;gap:8px;"><input type="number" id="dist" value="5" min="0.1" step="0.1" style="flex:1;"><select id="unit" style="width:80px;"><option value="km">km</option><option value="mi" selected>miles</option></select></div></div>
<div id="paceInputs" style="display:none;">
<div class="form-row">
<div class="form-group"><label>Min/Mile or Min/km</label><input type="number" id="paceMin" value="8" min="1" max="30"></div>
<div class="form-group"><label>Seconds</label><input type="number" id="paceSec" value="0" min="0" max="59"></div>
</div>
</div>
<button class="btn-calculate" onclick="calcPace()">Calculate</button>
</div>
<div class="calc-content">
<h2>How to Calculate Running Pace</h2>
<p><strong>Pace (min/mile) = Total Minutes / Miles</strong></p>
<p>Example: 5K (3.1 miles) in 28:30. Pace = 28.5 / 3.1 = 9:11 min/mile. Or 28.5 / 5 = 5:42 min/km.</p>
<h2>Common Race Pace Chart</h2>
<table class="schedule-table"><thead><tr><th>Distance</th><th>7:00/mi</th><th>8:00/mi</th><th>9:00/mi</th><th>10:00/mi</th></tr></thead><tbody>
<tr><td>5K</td><td>21:46</td><td>24:52</td><td>27:58</td><td>31:04</td></tr>
<tr><td>10K</td><td>43:31</td><td>49:44</td><td>55:56</td><td>1:02:08</td></tr>
<tr><td>Half Marathon</td><td>1:31:41</td><td>1:44:46</td><td>1:57:52</td><td>2:10:58</td></tr>
<tr><td>Marathon</td><td>3:03:20</td><td>3:29:23</td><td>3:55:26</td><td>4:21:29</td></tr>
</tbody></table>
<h2>Pace Zone Training</h2>
<ul><li><strong>Easy (Zone 2)</strong>: 65-75% max HR — builds aerobic base</li><li><strong>Threshold</strong>: 80-88% max HR — improves lactate clearance</li><li><strong>Intervals</strong>: 90-100% max HR — improves VO2 max and speed</li></ul>
</div></div>
<div class="results-panel"><h2>Results</h2>
<div class="result-item"><div class="result-label">Pace per Mile</div><div class="result-value" id="paceMile">---</div></div>
<div class="result-item"><div class="result-label">Pace per KM</div><div class="result-value secondary" id="paceKm">---</div></div>
<div class="result-item"><div class="result-label">Speed (mph)</div><div class="result-value secondary" id="speedMph">---</div></div>
<div class="result-item"><div class="result-label">5K Time</div><div class="result-value secondary" id="time5k">---</div></div>
<div class="result-item"><div class="result-label">10K Time</div><div class="result-value secondary" id="time10k">---</div></div>
<div class="result-item"><div class="result-label">Half Marathon</div><div class="result-value secondary" id="timeHalf">---</div></div>
<div class="result-item"><div class="result-label">Marathon</div><div class="result-value secondary" id="timeMarathon">---</div></div>
</div></div></div>""" + """
<script>
function fmtTime(s){
  const h=Math.floor(s/3600),m=Math.floor((s%3600)/60),sec=Math.round(s%60);
  return h>0?h+':'+String(m).padStart(2,'0')+':'+String(sec).padStart(2,'0'):m+':'+String(sec).padStart(2,'0');
}
function togglePace(){
  const by=document.getElementById('calcBy').value;
  document.getElementById('paceInputs').style.display=by==='pace'?'block':'none';
}
function calcPace(){
  const by=document.getElementById('calcBy').value;
  let totalMin;
  if(by==='time'){
    const h=parseFloat(document.getElementById('ph').value)||0;
    const m=parseFloat(document.getElementById('pm').value)||0;
    const s=parseFloat(document.getElementById('ps').value)||0;
    totalMin=h+m+s/60;
  }else{
    const pm=parseFloat(document.getElementById('paceMin').value)||8;
    const ps=parseFloat(document.getElementById('paceSec').value)||0;
    const dist=parseFloat(document.getElementById('dist').value)||1;
    totalMin=(pm+ps/60)*dist;
  }
  const dist=parseFloat(document.getElementById('dist').value)||1;
  const isMi=document.getElementById('unit').value==='mi';
  const kmDist=isMi?dist*1.60934:dist;
  const miDist=isMi?dist:dist/1.60934;
  const paceMi=totalMin/miDist;
  const paceKm=totalMin/kmDist;
  const mph=60/paceMi;
  document.getElementById('paceMile').textContent=Math.floor(paceMi)+':'+String(Math.round((paceMi%1)*60)).padStart(2,'0')+' /mi';
  document.getElementById('paceKm').textContent=Math.floor(paceKm)+':'+String(Math.round((paceKm%1)*60)).padStart(2,'0')+' /km';
  document.getElementById('speedMph').textContent=mph.toFixed(1)+' mph';
  document.getElementById('time5k').textContent=fmtTime(paceKm*5);
  document.getElementById('time10k').textContent=fmtTime(paceKm*10);
  document.getElementById('timeHalf').textContent=fmtTime(paceKm*21.0975);
  document.getElementById('timeMarathon').textContent=fmtTime(paceKm*42.195);
}
calcPace();
</script>""" + FOOT)

# ── MACRO CALCULATOR ──
w(os.path.join(SITE_DIR,"macro-calculator.html"), HEAD + """
<title>Macro Calculator - Free Carb Protein Fat Calculator 2026 | CalcWithMe</title>
<meta name="description" content="Free macro calculator. Calculate your daily carbohydrate, protein, and fat intake based on your calorie goal and fitness goal.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/macro-calculator.html">
<meta property="og:title" content="Macro Calculator - CalcWithMe">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What are macros?","acceptedAnswer":{"@type":"Answer","text":"Macros (macronutrients) are the three main nutrients: carbohydrates (4 cal/g), protein (4 cal/g), and fat (9 cal/g). They make up all the calories you eat."}},{"@type":"Question","name":"How much protein do I need?","acceptedAnswer":{"@type":"Answer","text":"0.8g/kg body weight for sedentary adults. Athletes: 1.4-2.0g/kg. People building muscle: 1.6-2.2g/kg."}}]}</script>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Macro Calculator</h1>
<p class="page-desc">Calculate your daily carbohydrate, protein, and fat targets based on your calorie goal and fitness goal.</p>
<div class="calc-form">
<div class="form-group"><label>Goal</label><select id="goal"><option value="lose">Lose Weight (Cut)</option><option value="maintain">Maintain Weight</option><option value="gain">Build Muscle (Bulk)</option></select></div>
<div class="form-row">
<div class="form-group"><label>Weight (lbs)</label><input type="number" id="weight" value="160" min="80" max="400"></div>
<div class="form-group"><label>Activity Level</label><select id="activity">
<option value="1.2">Sedentary</option><option value="1.375">Light (1-3x/week)</option><option value="1.55" selected>Moderate (3-5x/week)</option>
<option value="1.725">Active (6-7x/week)</option><option value="1.9">Very Active (Athletic)</option>
</select></div>
</div>
<div class="form-group"><label>Macro Split</label><select id="split">
<option value="balanced">Balanced (40/30/30 - C/P/F)</option>
<option value="lowcarb">Low Carb (25/40/35 - C/P/F)</option>
<option value="highcarb">High Carb (50/25/25 - C/P/F)</option>
<option value="keto">Keto (5/35/60 - C/P/F)</option>
<option value="paleo">Paleo (30/35/35 - C/P/F)</option>
</select></div>
<button class="btn-calculate" onclick="calcMacro()">Calculate Macros</button>
</div>
<div class="calc-content">
<h2>What Are Macros?</h2>
<p>Macronutrients are the nutrients that provide calories: Carbohydrates (4 cal/g), Protein (4 cal/g), Fat (9 cal/g). Your macro split determines what proportion of each you eat.</p>
<h2>Common Macro Splits</h2>
<ul><li><strong>Balanced (40/30/30)</strong>: Good general-purpose split</li><li><strong>Low Carb (25/40/35)</strong>: Better for fat loss and blood sugar control</li><li><strong>High Carb (50/25/25)</strong>: Ideal for endurance athletes and high-intensity training</li><li><strong>Keto (5/35/60)</strong>: Very low carb, high fat for ketone production</li></ul>
<h2>Protein: The Most Important Macro</h2>
<p>Protein is the most satiating macro and essential for muscle repair. Target: 1.6-2.2g/kg body weight for muscle building, 1.2-1.6g/kg for weight loss to preserve muscle mass.</p>
<h2>Pre- vs Post-Workout Nutrition</h2>
<ul><li><strong>Before workout</strong>: 0.5g carbs/lb body weight 1-2 hours before</li><li><strong>After workout</strong>: 20-40g protein within 2 hours post-workout</li></ul>
</div></div>
<div class="results-panel"><h2>Daily Macro Targets</h2>
<div class="result-item"><div class="result-label">Daily Calories</div><div class="result-value" id="calories">---</div></div>
<div class="result-item"><div class="result-label">Carbohydrates</div><div class="result-value" id="carbs">---</div></div>
<div class="result-item"><div class="result-label">Protein</div><div class="result-value secondary" id="protein">---</div></div>
<div class="result-item"><div class="result-label">Fat</div><div class="result-value secondary" id="fat">---</div></div>
<div class="result-item"><div class="result-label">Carbs (grams)</div><div class="result-value secondary" id="carbsG">---</div></div>
<div class="result-item"><div class="result-label">Protein (grams)</div><div class="result-value secondary" id="proteinG">---</div></div>
<div class="result-item"><div class="result-label">Fat (grams)</div><div class="result-value secondary" id="fatG">---</div></div>
</div></div></div>""" + """
<script>
function calcMacro(){
  const w=parseFloat(document.getElementById('weight').value)||160;
  const act=parseFloat(document.getElementById('activity').value)||1.55;
  const goal=document.getElementById('goal').value;
  const split=document.getElementById('split').value;
  const bmr=w*10+6.25*170-5*30+5; // approx
  const tdee=bmr*act;
  let calories=goal==='lose'?tdee-500:goal==='gain'?tdee+300:tdee;
  const splits={'balanced':[0.4,0.3,0.3],'lowcarb':[0.25,0.4,0.35],'highcarb':[0.5,0.25,0.25],'keto':[0.05,0.35,0.6],'paleo':[0.3,0.35,0.35]};
  const [cPct,pPct,fPct]=splits[split];
  const carbs=cPct*calories/4,protein=pPct*calories/4,fat=fPct*calories/9;
  document.getElementById('calories').textContent=Math.round(calories)+' cal/day';
  document.getElementById('carbs').textContent=(cPct*100)+'% = '+Math.round(carbs)+' cal';
  document.getElementById('protein').textContent=(pPct*100)+'% = '+Math.round(protein)+' cal';
  document.getElementById('fat').textContent=(fPct*100)+'% = '+Math.round(fat)+' cal';
  document.getElementById('carbsG').textContent=Math.round(carbs)+'g';
  document.getElementById('proteinG').textContent=Math.round(protein)+'g';
  document.getElementById('fatG').textContent=Math.round(fat)+'g';
}
calcMacro();
</script>""" + FOOT)

# ── WATER INTAKE CALCULATOR ──
w(os.path.join(SITE_DIR,"water-calculator.html"), HEAD + """
<title>Water Intake Calculator - Daily Hydration Needs Calculator | CalcWithMe</title>
<meta name="description" content="Free water intake calculator. Find out how much water you should drink daily based on your weight, activity level, and climate.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/water-calculator.html">
<meta property="og:title" content="Water Intake Calculator - CalcWithMe">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How much water should I drink per day?","acceptedAnswer":{"@type":"Answer","text":"A common guideline is 8 glasses (64 oz) daily, but your actual need depends on weight (0.5-1 oz per lb), activity level, and climate."}},{"@type":"Question","name":"What are signs of dehydration?","acceptedAnswer":{"@type":"Answer","text":"Mild dehydration: thirst, dark urine, fatigue, headache. Severe: dizziness, rapid heartbeat, confusion, very dark urine."}}]}</script>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Water Intake Calculator</h1>
<p class="page-desc">Find out how much water you should drink daily based on your weight, activity level, and climate.</p>
<div class="calc-form">
<div class="form-group"><label>Weight (lbs)</label><input type="number" id="weight" value="160" min="50" max="500"></div>
<div class="form-row">
<div class="form-group"><label>Activity Level</label><select id="activity">
<option value="0.5">Sedentary</option><option value="0.6" selected>Moderate (3-5x/week)</option>
<option value="0.7">Active (daily)</option><option value="0.8">Very Active (intense daily)</option>
</select></div>
<div class="form-group"><label>Climate</label><select id="climate">
<option value="1" selected>Moderate</option><option value="1.15">Hot/Humid</option>
<option value="0.9">Cold/Dry</option>
</select></div>
</div>
<button class="btn-calculate" onclick="calcWater()">Calculate Water Needs</button>
</div>
<div class="calc-content">
<h2>How Much Water Do You Really Need?</h2>
<p>The old "8 glasses a day" rule is a rough estimate. More accurate: drink <strong>0.5 to 1 ounce per pound</strong> of body weight. A 160 lb person needs 80-160 oz/day depending on activity.</p>
<h2>Signs You're Not Drinking Enough</h2>
<ul><li>Dark yellow urine (should be pale yellow)</li><li>Fatigue and low energy</li><li>Headaches</li><li>Dry skin and lips</li><li>Constipation</li><li>Dizziness</li></ul>
<h2>Water vs Other Beverages</h2>
<p>Plain water is best but all fluids count toward hydration: tea, coffee, milk, and even caffeinated beverages contribute. About 20% of water intake comes from food (especially fruits and vegetables).</p>
<h2>When to Drink More</h2>
<ul><li>During and after exercise</li><li>Hot or humid weather</li><li>Illness (fever, vomiting, diarrhea)</li><li>Pregnancy and breastfeeding</li><li>High altitude</li></ul>
</div></div>
<div class="results-panel"><h2>Your Daily Water Needs</h2>
<div class="result-item"><div class="result-label">Minimum</div><div class="result-value" id="waterMin">---</div></div>
<div class="result-item"><div class="result-label">Recommended</div><div class="result-value" id="waterRec">---</div></div>
<div class="result-item"><div class="result-label">Active Days</div><div class="result-value secondary" id="waterActive">---</div></div>
<div class="result-item"><div class="result-label">Glasses (8oz each)</div><div class="result-value secondary" id="glasses">---</div></div>
</div></div></div>""" + """
<script>
function calcWater(){
  const w=parseFloat(document.getElementById('weight').value)||160;
  const act=parseFloat(document.getElementById('activity').value)||0.6;
  const climate=parseFloat(document.getElementById('climate').value)||1;
  const base=w*act*climate;
  const min=Math.round(w*0.5);
  const rec=Math.round(base);
  const active=Math.round(base*1.25);
  document.getElementById('waterMin').textContent=min+' oz ('+(min/33.814).toFixed(1)+' L)';
  document.getElementById('waterRec').textContent=rec+' oz ('+(rec/33.814).toFixed(1)+' L)';
  document.getElementById('waterActive').textContent=active+' oz ('+(active/33.814).toFixed(1)+' L)';
  document.getElementById('glasses').textContent=Math.round(rec/8)+' glasses (8 oz each)';
}
calcWater();
</script>""" + FOOT)

# ── HEART RATE ZONE CALCULATOR ──
w(os.path.join(SITE_DIR,"heart-rate-calculator.html"), HEAD + """
<title>Heart Rate Zone Calculator - Target Heart Rate 2026 | CalcWithMe</title>
<meta name="description" content="Free heart rate zone calculator. Find your target heart rate zones for different exercise intensities using the Karvonen formula.">
<meta name="robots" content="index,follow"><link rel="canonical" href="https://calcwithme.com/heart-rate-calculator.html">
<meta property="og:title" content="Heart Rate Zone Calculator - CalcWithMe">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is my target heart rate?","acceptedAnswer":{"@type":"Answer","text":"Your target heart rate for exercise is 50-85% of your maximum heart rate (220 - age). Use the Karvonen formula for more accuracy."}},{"@type":"Question","name":"How do I measure my heart rate?","acceptedAnswer":{"@type":"Answer","text":"Place two fingers on your wrist or neck, count beats for 15 seconds, multiply by 4 for beats per minute."}}]}</script>
</head>
<body>""" + NAV + """
<main class="calculator-page"><div class="container"><div class="calculator-layout">
<div class="calculator-main">
<h1>Heart Rate Zone Calculator</h1>
<p class="page-desc">Calculate your target heart rate zones for different exercise intensities. Uses the Karvonen formula for accuracy.</p>
<div class="calc-form">
<div class="form-group"><label>Age (years)</label><input type="number" id="age" value="30" min="15" max="100"></div>
<div class="form-group"><label>Resting Heart Rate (bpm)</label><input type="number" id="rhr" value="70" min="40" max="120"><div class="help-text">Measure in the morning before getting up</div></div>
<div class="form-group"><label>Formula</label><select id="formula"><option value="karvonen" selected>Karvonen (recommended)</option><option value="simple">Simple (220-age)</option></select></div>
<button class="btn-calculate" onclick="calcHR()">Calculate Heart Rate Zones</button>
</div>
<div class="calc-content">
<h2>Understanding Heart Rate Zones</h2>
<p>Exercise at different heart rate zones produces different benefits. Train across zones for optimal fitness.</p>
<h2>Heart Rate Zones (by % of Max)</h2>
<ul><li><strong>Zone 1 (50-60%)</strong>: Very light — recovery walks, warm-up, cool-down</li><li><strong>Zone 2 (60-70%)</strong>: Light — fat burning, builds aerobic base, easy conversation</li><li><strong>Zone 3 (70-80%)</strong>: Moderate — aerobic endurance, improves cardiovascular fitness</li><li><strong>Zone 4 (80-90%)</strong>: Hard — anaerobic threshold, improves speed and performance</li><li><strong>Zone 5 (90-100%)</strong>: Maximum — interval training, short bursts, improves VO2 max</li></ul>
<h2>The Karvonen Formula</h2>
<p><strong>Target HR = ((Max HR - Resting HR) x %Intensity) + Resting HR</strong></p>
<p>This formula is more accurate than the simple 220-age method because it accounts for your fitness level (resting heart rate).</p>
<h2>How to Measure Your Resting Heart Rate</h2>
<p>Measure first thing in the morning before getting out of bed. Count your pulse for 60 seconds (or 30 seconds x 2). Lower resting HR = better fitness. Athletes often have RHR of 40-60 bpm.</p>
</div></div>
<div class="results-panel"><h2>Your Heart Rate Zones</h2>
<div class="result-item"><div class="result-label">Max Heart Rate</div><div class="result-value" id="maxHR">---</div></div>
<div class="result-item"><div class="result-label">Zone 1 (50-60%)</div><div class="result-value secondary" id="zone1">---</div></div>
<div class="result-item"><div class="result-label">Zone 2 (60-70%)</div><div class="result-value secondary" id="zone2">---</div></div>
<div class="result-item"><div class="result-label">Zone 3 (70-80%)</div><div class="result-value secondary" id="zone3">---</div></div>
<div class="result-item"><div class="result-label">Zone 4 (80-90%)</div><div class="result-value secondary" id="zone4">---</div></div>
<div class="result-item"><div class="result-label">Zone 5 (90-100%)</div><div class="result-value secondary" id="zone5">---</div></div>
</div></div></div>""" + """
<script>
function calcHR(){
  const age=parseFloat(document.getElementById('age').value)||30;
  const rhr=parseFloat(document.getElementById('rhr').value)||70;
  const formula=document.getElementById('formula').value;
  const maxHR=formula==='karvonen'?220-age:220-age;
  const zones=[0.5,0.6,0.7,0.8,0.9];
  const names=['zone1','zone2','zone3','zone4','zone5'];
  const labels=['Zone 1 (50-60%)','Zone 2 (60-70%)','Zone 3 (70-80%)','Zone 4 (80-90%)','Zone 5 (90-100%)'];
  document.getElementById('maxHR').textContent=maxHR+' bpm';
  zones.forEach((z,i)=>{
    let thr;
    if(formula==='karvonen'){
      thr=(maxHR-rhr)*z+rhr;
    }else{
      thr=maxHR*z;
    }
    document.getElementById(names[i]).textContent=Math.round(thr)+' bpm';
  });
}
calcHR();
</script>""" + FOOT)

print("All 8 health calculators created!")

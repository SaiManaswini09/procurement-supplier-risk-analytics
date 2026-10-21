from pathlib import Path
import pandas as pd
import json

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUTPUT = ROOT / "dashboard" / "index.html"

df = pd.read_csv(DATA / "procurement_data.csv")
suppliers = pd.read_csv(DATA / "supplier_kpis.csv")

# Keep the HTML reasonably small while embedding the complete analytical data.
records = df.to_dict(orient="records")
supplier_records = suppliers.to_dict(orient="records")

data_json = json.dumps(records, separators=(",", ":"))
supplier_json = json.dumps(supplier_records, separators=(",", ":"))

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Procurement Intelligence Dashboard</title>

<style>
*{box-sizing:border-box}
body{
    margin:0;
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
    background:#f3f6fb;
    color:#172033
}
.hero{
    background:linear-gradient(120deg,#0f172a,#172554,#1e3a8a);
    color:white;
    padding:38px 6%
}
.hero-top{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:20px
}
.eyebrow{
    font-size:12px;
    letter-spacing:2px;
    font-weight:700;
    color:#93c5fd
}
h1{font-size:38px;margin:8px 0}
.hero p{color:#cbd5e1;max-width:800px}
.badge{
    border:1px solid #ffffff40;
    padding:9px 15px;
    border-radius:20px;
    white-space:nowrap
}
main{
    width:min(1450px,92%);
    margin:25px auto
}
.panel{
    background:white;
    border:1px solid #e2e8f0;
    border-radius:14px;
    padding:22px;
    box-shadow:0 4px 16px #0f172a0d;
    margin-bottom:20px
}
.filter-head{
    display:flex;
    justify-content:space-between;
    align-items:center
}
.filter-head h2{margin:0}
.filters{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:15px;
    margin-top:18px
}
label{
    display:block;
    font-size:12px;
    font-weight:700;
    color:#64748b;
    margin-bottom:6px
}
select{
    width:100%;
    padding:11px;
    border:1px solid #cbd5e1;
    border-radius:8px;
    background:white
}
button{
    padding:10px 14px;
    border-radius:8px;
    border:1px solid #cbd5e1;
    background:white;
    cursor:pointer
}
.kpis{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:16px;
    margin-bottom:20px
}
.kpi{
    background:white;
    padding:20px;
    border-radius:13px;
    border:1px solid #e2e8f0;
    box-shadow:0 4px 16px #0f172a0d
}
.kpi .label{
    font-size:12px;
    color:#64748b;
    font-weight:700
}
.kpi .value{
    font-size:28px;
    font-weight:750;
    margin:10px 0 5px
}
.kpi small{color:#64748b}
.insight{
    border-left:5px solid #2563eb
}
.insight h2{margin:7px 0}
.insight p{color:#64748b;line-height:1.6}
.grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:20px
}
.chart-title{
    font-weight:700;
    margin-bottom:18px
}
.bar-row{
    display:grid;
    grid-template-columns:90px 1fr 95px;
    gap:10px;
    align-items:center;
    margin:11px 0;
    font-size:13px
}
.track{
    background:#eef2f7;
    height:14px;
    border-radius:7px;
    overflow:hidden
}
.bar{
    height:100%;
    background:linear-gradient(90deg,#2563eb,#60a5fa);
    border-radius:7px
}
.bar.red{
    background:linear-gradient(90deg,#dc2626,#fb7185)
}
.right{text-align:right}
.risk-table{
    width:100%;
    border-collapse:collapse
}
.risk-table th{
    color:#64748b;
    font-size:12px;
    text-align:left;
    padding:10px;
    border-bottom:1px solid #e2e8f0
}
.risk-table td{
    padding:11px 10px;
    border-bottom:1px solid #eef2f7;
    font-size:13px
}
.risk{
    padding:5px 9px;
    border-radius:20px;
    font-size:11px;
    font-weight:700
}
.High{background:#fee2e2;color:#b91c1c}
.Medium{background:#ffedd5;color:#c2410c}
.Low{background:#dcfce7;color:#15803d}
.sim{
    display:grid;
    grid-template-columns:1fr 1fr;
    align-items:center;
    gap:40px
}
input[type=range]{width:100%}
.saving{
    font-size:32px;
    font-weight:800;
    color:#15803d;
    margin-top:10px
}
footer{
    text-align:center;
    color:#64748b;
    font-size:12px;
    padding:30px
}
@media(max-width:900px){
    .kpis{grid-template-columns:repeat(2,1fr)}
    .grid,.sim{grid-template-columns:1fr}
}
@media(max-width:600px){
    .filters,.kpis{grid-template-columns:1fr}
    .hero-top{display:block}
    h1{font-size:28px}
}
</style>
</head>

<body>

<header class="hero">
<div class="hero-top">
<div>
<div class="eyebrow">PROCUREMENT INTELLIGENCE</div>
<h1>Cost, Performance & Supplier Risk</h1>
<p>Executive analytics across procurement spend, purchase price variance, delivery performance and supplier risk.</p>
</div>
<div class="badge">10,000 Purchase Orders</div>
</div>
</header>

<main>

<section class="panel">
<div class="filter-head">
<div>
<div class="eyebrow" style="color:#2563eb">ANALYSIS CONTROLS</div>
<h2>Procurement Portfolio</h2>
</div>
<button id="reset">Reset Filters</button>
</div>

<div class="filters">
<div><label>SUPPLIER</label><select id="supplier"><option>All</option></select></div>
<div><label>PLANT</label><select id="plant"><option>All</option></select></div>
<div><label>CATEGORY</label><select id="category"><option>All</option></select></div>
</div>
</section>

<section class="kpis">
<div class="kpi"><div class="label">TOTAL SPEND</div><div class="value" id="spend">—</div><small>Actual procurement spend</small></div>
<div class="kpi"><div class="label">TOTAL PPV</div><div class="value" id="ppv">—</div><small>Actual vs forecast</small></div>
<div class="kpi"><div class="label">PPV %</div><div class="value" id="ppvpct">—</div><small>Cost variance rate</small></div>
<div class="kpi"><div class="label">ON-TIME DELIVERY</div><div class="value" id="otd">—</div><small>Supplier delivery performance</small></div>
<div class="kpi"><div class="label">HIGH-RISK SUPPLIERS</div><div class="value" id="riskcount">—</div><small>Require attention</small></div>
</section>

<section class="panel insight">
<div class="eyebrow" style="color:#2563eb">EXECUTIVE INSIGHT</div>
<h2 id="insightTitle"></h2>
<p id="insight"></p>
</section>

<div class="grid">
<section class="panel">
<div class="eyebrow" style="color:#2563eb">COST PERFORMANCE</div>
<div class="chart-title">Top Suppliers by Unfavorable PPV</div>
<div id="supplierBars"></div>
</section>

<section class="panel">
<div class="eyebrow" style="color:#2563eb">CATEGORY ANALYSIS</div>
<div class="chart-title">Purchase Price Variance by Category</div>
<div id="categoryBars"></div>
</section>
</div>

<section class="panel sim">
<div>
<div class="eyebrow" style="color:#2563eb">SOURCING OPPORTUNITY</div>
<h2>Negotiation Savings Simulator</h2>
<p style="color:#64748b">Estimate savings from negotiated reductions against current filtered procurement spend.</p>
</div>
<div>
<label>NEGOTIATED PRICE REDUCTION: <span id="rate">5%</span></label>
<input id="slider" type="range" min="1" max="15" value="5">
<div class="saving" id="saving"></div>
</div>
</section>

<section class="panel">
<div class="eyebrow" style="color:#2563eb">SUPPLIER PERFORMANCE</div>
<h2>Supplier Risk Overview</h2>
<div style="overflow:auto">
<table class="risk-table">
<thead>
<tr>
<th>Supplier</th>
<th>Spend</th>
<th>PPV</th>
<th>PPV %</th>
<th>OTD %</th>
<th>POs</th>
<th>Risk</th>
</tr>
</thead>
<tbody id="supplierTable"></tbody>
</table>
</div>
</section>

</main>

<footer>Procurement Intelligence Portfolio · Synthetic Data · Python + JavaScript Analytics</footer>

<script>
const DATA = __DATA__;
const SUPPLIER_KPIS = __SUPPLIERS__;

const euro = n => new Intl.NumberFormat("en-DE",{
 style:"currency",currency:"EUR",maximumFractionDigits:0
}).format(n);

const compact = n => new Intl.NumberFormat("en",{
 notation:"compact",maximumFractionDigits:1
}).format(n);

const unique = field => [...new Set(DATA.map(d=>d[field]))].sort();

function fill(id,field){
 const el=document.getElementById(id);
 unique(field).forEach(v=>{
  const o=document.createElement("option");
  o.value=v;o.textContent=v;el.appendChild(o);
 });
}

fill("supplier","supplier");
fill("plant","plant");
fill("category","category");

function filtered(){
 const s=document.getElementById("supplier").value;
 const p=document.getElementById("plant").value;
 const c=document.getElementById("category").value;
 return DATA.filter(d=>
  (s==="All"||d.supplier===s)&&
  (p==="All"||d.plant===p)&&
  (c==="All"||d.category===c)
 );
}

function supplierAgg(rows){
 const m={};
 rows.forEach(d=>{
  if(!m[d.supplier])m[d.supplier]={supplier:d.supplier,spend:0,ppv:0,pos:0,count:0};
  const x=m[d.supplier];
  x.spend+=+d.actual_spend;
  x.ppv+=+d.ppv;
  x.pos+=+d.on_time;
  x.count++;
 });
 return Object.values(m).map(x=>{
  x.otd=x.count?100*x.pos/x.count:0;
  x.ppvpct=x.spend?100*x.ppv/x.spend:0;
  x.risk=(x.ppvpct>4||x.otd<70)?"High":(x.ppvpct>2||x.otd<85)?"Medium":"Low";
  return x;
 });
}

function bars(container,items,label,value,red=false){
 const root=document.getElementById(container);
 root.innerHTML="";
 const max=Math.max(...items.map(value),1);
 items.forEach(x=>{
  const r=document.createElement("div");
  r.className="bar-row";
  r.innerHTML=`<div>${label(x)}</div>
  <div class="track"><div class="bar ${red?"red":""}" style="width:${Math.max(2,100*value(x)/max)}%"></div></div>
  <div class="right">${euro(value(x))}</div>`;
  root.appendChild(r);
 });
}

function render(){
 const rows=filtered();

 const spend=rows.reduce((a,d)=>a+(+d.actual_spend),0);
 const forecast=rows.reduce((a,d)=>a+(+d.forecast_spend),0);
 const ppv=rows.reduce((a,d)=>a+(+d.ppv),0);
 const otd=rows.length?100*rows.reduce((a,d)=>a+(+d.on_time),0)/rows.length:0;
 const ppvpct=forecast?100*ppv/forecast:0;

 const sa=supplierAgg(rows).sort((a,b)=>b.ppv-a.ppv);
 const high=sa.filter(x=>x.risk==="High").length;

 document.getElementById("spend").textContent=euro(spend);
 document.getElementById("ppv").textContent=euro(ppv);
 document.getElementById("ppvpct").textContent=ppvpct.toFixed(2)+"%";
 document.getElementById("otd").textContent=otd.toFixed(1)+"%";
 document.getElementById("riskcount").textContent=high;

 if(sa.length){
  const w=sa[0];
  document.getElementById("insightTitle").textContent=w.supplier+" is the largest unfavorable PPV opportunity";
  document.getElementById("insight").textContent=
   `${w.supplier} contributes ${euro(w.ppv)} in PPV with ${w.otd.toFixed(1)}% on-time delivery. Prioritize this supplier for commercial review, sourcing negotiations and delivery-performance improvement.`;
 }

 bars("supplierBars",sa.slice(0,7),x=>x.supplier,x=>Math.max(x.ppv,0),true);

 const cm={};
 rows.forEach(d=>cm[d.category]=(cm[d.category]||0)+(+d.ppv));
 const cats=Object.entries(cm).map(([category,ppv])=>({category,ppv}))
  .sort((a,b)=>b.ppv-a.ppv);

 bars("categoryBars",cats,x=>x.category,x=>Math.max(x.ppv,0));

 const tbody=document.getElementById("supplierTable");
 tbody.innerHTML="";
 sa.forEach(x=>{
  const tr=document.createElement("tr");
  tr.innerHTML=`<td><b>${x.supplier}</b></td>
  <td>${euro(x.spend)}</td>
  <td>${euro(x.ppv)}</td>
  <td>${x.ppvpct.toFixed(2)}%</td>
  <td>${x.otd.toFixed(1)}%</td>
  <td>${x.count}</td>
  <td><span class="risk ${x.risk}">${x.risk}</span></td>`;
  tbody.appendChild(tr);
 });

 updateSaving(spend);
}

function updateSaving(spend=null){
 const rate=+document.getElementById("slider").value;
 document.getElementById("rate").textContent=rate+"%";
 if(spend===null)spend=filtered().reduce((a,d)=>a+(+d.actual_spend),0);
 document.getElementById("saving").textContent=euro(spend*rate/100)+" potential savings";
}

["supplier","plant","category"].forEach(id=>
 document.getElementById(id).addEventListener("change",render)
);

document.getElementById("slider").addEventListener("input",()=>updateSaving());

document.getElementById("reset").addEventListener("click",()=>{
 ["supplier","plant","category"].forEach(id=>document.getElementById(id).value="All");
 render();
});

render();
</script>

</body>
</html>
"""

html = html.replace("__DATA__", data_json)
html = html.replace("__SUPPLIERS__", supplier_json)

OUTPUT.parent.mkdir(exist_ok=True)
OUTPUT.write_text(html, encoding="utf-8")

print(f"Dashboard created: {OUTPUT}")
print(f"Purchase orders embedded: {len(df):,}")
print(f"Suppliers embedded: {len(suppliers):,}")
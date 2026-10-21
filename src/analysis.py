from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT/"data"/"procurement_data.csv", parse_dates=["po_date"])

supplier = df.groupby("supplier").agg(
    total_spend=("actual_spend","sum"), total_ppv=("ppv","sum"),
    avg_ppv_pct=("ppv_pct","mean"), otd_pct=("on_time","mean"),
    po_count=("po_id","count"), avg_late_days=("late_days","mean")
).reset_index()

supplier["otd_pct"] *= 100
u = supplier["total_ppv"].clip(lower=0)
supplier["ppv_risk_norm"] = 100*(u-u.min())/(u.max()-u.min())
supplier["late_delivery_rate"] = 100-supplier["otd_pct"]
supplier["risk_score"] = (.6*supplier["ppv_risk_norm"]+.4*supplier["late_delivery_rate"]).round(1)
supplier["risk_level"] = pd.cut(supplier["risk_score"],[-.1,30,60,100],labels=["Low","Medium","High"])
supplier = supplier.sort_values("risk_score",ascending=False)
supplier.to_csv(ROOT/"data"/"supplier_kpis.csv",index=False)

print("\nEXECUTIVE KPIs")
print(f"Total Spend: €{df.actual_spend.sum():,.0f}")
print(f"Total PPV: €{df.ppv.sum():,.0f}")
print(f"OTD: {df.on_time.mean()*100:.1f}%")
print("\nTOP SUPPLIER RISKS")
print(supplier[["supplier","total_ppv","otd_pct","risk_score","risk_level"]].head(10).to_string(index=False))

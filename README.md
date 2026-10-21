# Procurement Cost & Supplier Risk Analytics

A GitHub portfolio project demonstrating **Python, SQL, procurement analytics, PPV, supplier performance, and BI storytelling** with 10,000 synthetic purchase-order transactions.

> **Privacy:** This repository uses fully synthetic data. No employer, customer, supplier, or confidential business data is included.

## Business Problem
A manufacturing company purchases raw materials from multiple suppliers and plants. Procurement leadership needs to identify:
- suppliers and materials driving unfavorable Purchase Price Variance (PPV),
- suppliers combining high cost pressure with weak delivery performance,
- supplier-material combinations to prioritize for negotiation,
- potential savings under different negotiation scenarios.

## Solution
The project combines procurement cost and delivery metrics into an explainable supplier-risk framework.

**KPIs:** Total Spend, PPV, PPV %, OTD %, Late Delivery Rate, Supplier Risk Score, Potential Savings.

## Synthetic Dataset Snapshot
- Purchase orders: **10,000**
- Suppliers: **20**
- Materials: **50**
- Plants: **5**
- Total spend: **€50,977,186**
- Total PPV: **€1,416,875**
- OTD: **34.9%**
- High-risk suppliers: **2**
- Highest modeled risk: **SUP014**

## Methodology
```text
PPV = (Actual Price - Forecast Price) × Quantity

Supplier Risk Score =
60% × Normalized Unfavorable PPV
+ 40% × Late Delivery Rate
```

Risk bands: 0–30 Low | >30–60 Medium | >60 High.

## Repository Structure
```text
procurement-supplier-risk-analytics/
├── README.md
├── requirements.txt
├── LICENSE
├── data/
│   ├── procurement_data.csv
│   └── supplier_kpis.csv
├── notebooks/
│   └── procurement_analysis.ipynb
├── src/
│   ├── analysis.py
│   └── generate_data.py
├── sql/
│   └── procurement_analysis.sql
└── dashboard/
    └── DASHBOARD_BUILD_GUIDE.md
```

## Run Locally
```bash
git clone <your-repository-url>
cd procurement-supplier-risk-analytics
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/analysis.py
jupyter notebook notebooks/procurement_analysis.ipynb
```

## Analysis Included
1. Executive procurement KPIs
2. Supplier PPV analysis
3. Cost vs delivery supplier-risk scoring
4. Supplier risk matrix
5. Category-level cost drivers
6. Supplier-material negotiation targets
7. Monthly Actual vs Forecast analysis
8. 3%, 5%, and 10% what-if savings scenarios

## Dashboard Design
Build the supplied CSV in Tableau Public or Power BI.

```text
┌──────────────┬──────────────┬───────────┬───────────────────┐
│ Total Spend  │ Total PPV    │ OTD %     │ High-Risk Supp.   │
├──────────────┴──────────────┴───────────┴───────────────────┤
│                  Actual vs Forecast Trend                    │
├──────────────────────────────┬───────────────────────────────┤
│ PPV by Supplier              │ Supplier Risk Matrix          │
├──────────────────────────────┼───────────────────────────────┤
│ PPV by Category              │ Negotiation Opportunities     │
└──────────────────────────────┴───────────────────────────────┘
```

## Project Description
> I built a synthetic procurement analytics project around a common supply-chain problem: determining whether suppliers are performing against both cost and delivery expectations. I calculated purchase-price variance, analyzed on-time delivery, developed an explainable supplier-risk score, and added a what-if negotiation model. Python handles the analysis, SQL answers core business questions, and the dataset is designed for an executive Tableau or Power BI dashboard.

## Next Improvements
- Supplier quality/rejection rates
- Lead-time variability
- Commodity inflation indices
- Material-price forecasting
- PostgreSQL data layer
- Streamlit front end
- Automated data-quality tests

## Disclaimer
This is an independent portfolio project using synthetic data and does not reproduce confidential logic, data, or intellectual property from any employer.

# Tableau / Power BI Dashboard Guide

## Page 1 — Executive Overview
KPI cards: Total Spend | Total PPV | OTD % | High-Risk Suppliers

Visuals:
- Monthly Actual vs Forecast Spend
- Unfavorable PPV by Supplier
- PPV by Category
- Supplier Risk Matrix: X = Total PPV, Y = OTD %, Size = Spend

Filters: Date, Plant, Category, Supplier

## Page 2 — Supplier Deep Dive
- Supplier KPI table
- PPV monthly trend
- Material-level PPV
- OTD trend
- Top late deliveries

## Tableau calculated fields
PPV:
`([actual_price] - [forecast_price]) * [quantity]`

OTD:
`IF [delivery_days] <= [promised_days] THEN 1 ELSE 0 END`

5% Negotiation Savings:
`IF [PPV] > 0 THEN [actual_spend] * 0.05 ELSE 0 END`

Publish to Tableau Public and place the dashboard URL and screenshot in the README.

-- 1. Executive KPIs
SELECT
 SUM(actual_price * quantity) AS total_spend,
 SUM((actual_price - forecast_price) * quantity) AS total_ppv,
 100.0 * AVG(CASE WHEN delivery_days <= promised_days THEN 1.0 ELSE 0.0 END) AS otd_pct,
 COUNT(DISTINCT supplier) AS supplier_count
FROM procurement_transactions;

-- 2. Supplier performance
SELECT supplier,
 SUM(actual_price * quantity) AS total_spend,
 SUM((actual_price - forecast_price) * quantity) AS total_ppv,
 AVG(100.0*(actual_price-forecast_price)/NULLIF(forecast_price,0)) AS avg_ppv_pct,
 100.0*AVG(CASE WHEN delivery_days <= promised_days THEN 1.0 ELSE 0.0 END) AS otd_pct,
 COUNT(*) AS po_count
FROM procurement_transactions
GROUP BY supplier
ORDER BY total_ppv DESC;

-- 3. Category cost drivers
SELECT category,
 SUM(actual_price*quantity) AS actual_spend,
 SUM((actual_price-forecast_price)*quantity) AS total_ppv
FROM procurement_transactions
GROUP BY category
ORDER BY total_ppv DESC;

-- 4. Negotiation targets
SELECT supplier, material,
 SUM(quantity) AS total_quantity,
 SUM(actual_price*quantity) AS total_spend,
 SUM((actual_price-forecast_price)*quantity) AS total_ppv,
 100.0*AVG(CASE WHEN delivery_days <= promised_days THEN 1.0 ELSE 0.0 END) AS otd_pct
FROM procurement_transactions
GROUP BY supplier, material
HAVING SUM(actual_price*quantity) > 25000
ORDER BY total_ppv DESC;

-- 5. Monthly actual vs forecast
SELECT EXTRACT(YEAR FROM po_date) AS year, EXTRACT(MONTH FROM po_date) AS month,
 SUM(forecast_price*quantity) AS forecast_spend,
 SUM(actual_price*quantity) AS actual_spend,
 SUM((actual_price-forecast_price)*quantity) AS ppv
FROM procurement_transactions
GROUP BY EXTRACT(YEAR FROM po_date), EXTRACT(MONTH FROM po_date)
ORDER BY year, month;

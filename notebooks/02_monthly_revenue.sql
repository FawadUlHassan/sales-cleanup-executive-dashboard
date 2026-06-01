-- Monthly Revenue Trend

SELECT
    DATE_TRUNC('month', invoicedate::TIMESTAMP) AS sales_month,
    ROUND(SUM(revenue), 2) AS monthly_revenue,
    COUNT(DISTINCT invoiceno) AS monthly_orders,
    SUM(quantity) AS monthly_quantity_sold
FROM clean_sales
GROUP BY sales_month
ORDER BY sales_month;
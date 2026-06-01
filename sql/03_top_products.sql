-- Top 10 Products by Revenue

SELECT
    stockcode,
    description,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(quantity) AS total_quantity_sold,
    COUNT(DISTINCT invoiceno) AS order_count
FROM clean_sales
GROUP BY stockcode, description
ORDER BY total_revenue DESC
LIMIT 10;
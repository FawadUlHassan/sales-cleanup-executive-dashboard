-- Executive Sales KPIs
-- Source: data/processed/clean_sales.csv

SELECT
    ROUND(SUM(revenue), 2) AS total_revenue,
    COUNT(DISTINCT invoiceno) AS total_orders,
    COUNT(*) AS total_line_items,
    SUM(quantity) AS total_quantity_sold,
    ROUND(SUM(revenue) / COUNT(DISTINCT invoiceno), 2) AS average_order_value
FROM clean_sales;
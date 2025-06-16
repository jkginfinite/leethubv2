SELECT p.product_id,
IFNULL(ROUND(SUM(p.price*u.units)/SUM(u.units),2),0) as average_price
FROM prices as p
LEFT JOIN unitssold as u
ON p.product_id = u.product_id
AND u.purchase_date BETWEEN p.start_date and p.end_date
GROUP BY p.product_id
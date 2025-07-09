# Write your MySQL query statement below

select c.customer_id, customer_name
FROM customers c
LEFT JOIN orders
using (customer_id)
group by customer_id
HAVING SUM(product_name='A')>0 AND SUM(product_name='B')>0 AND SUM(product_name='C')=0
ORDER BY customer_id
# Write your MySQL query statement below
select customer_name, customer_id, order_id, order_date
from
(select name as customer_name, customer_id, order_id, order_date, RANK() over (partition by customer_id ORDER BY order_date DESC) as r
from customers
join orders
using (customer_id)) as x
where r<=3
order by customer_name ASC, customer_id ASC, order_date DESC
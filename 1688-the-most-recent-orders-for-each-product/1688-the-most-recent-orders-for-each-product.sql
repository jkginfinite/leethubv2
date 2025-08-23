# Write your MySQL query statement below
with t as
(select product_name, product_id, order_id, order_date
from orders 
join products
using (product_id)),

t2 as
(select product_name, product_id, max(order_date) as order_date
from t
group by 1,2)

select product_name, product_id, order_id, order_date
from t
join t2
using (product_name, product_id, order_date)
order by product_name ASC, product_id ASC, order_id ASC
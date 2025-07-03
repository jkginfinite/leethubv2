# Write your MySQL query statement below
with t1 as
(select customer_id, product_id, product_name, count(*) as c
from products
join orders
using (product_id)
group by 1,2,3),

t2 as
(select customer_id, max(c) as c
from t1
group by 1)

select customer_id, product_id, product_name 
from t2
inner join t1
using (customer_id, c)
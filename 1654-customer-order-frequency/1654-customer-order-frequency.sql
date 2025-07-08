# Write your MySQL query statement below
with t1 as
(select customer_id, name
from customers
join orders
using (customer_id)
join product
using (product_id)
where order_date like '2020-06%'
group by 1,2
having sum(price*quantity)>=100),
t2 as
(select customer_id, name
from customers
join orders
using (customer_id)
join product
using (product_id)
where order_date like '2020-07%'
group by 1,2
having sum(price*quantity)>=100)

select distinct *
from
(select *
from t1
where customer_id in (select customer_id from t2)
union all
select *
from t2
where customer_id in (select customer_id from t1)) X
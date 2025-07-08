# Write your MySQL query statement below
with t as
(select seller_id, sum(price) as p
from product
join sales
using (product_id)
group by 1
order by 2 DESC)

select seller_id
from t
where p in (select max(p) from t)
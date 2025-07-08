# Write your MySQL query statement below
with t as
(select buyer_id, product_name
from product
join sales
using (product_id))

select distinct(buyer_id) as buyer_id
from t
where buyer_id in (select buyer_id from t where product_name='S8')
and buyer_id not in (select buyer_id from t where product_name='iPhone')
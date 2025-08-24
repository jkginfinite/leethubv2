# Write your MySQL query statement below

with t as
(select user_id,product_id, sum(quantity*price) as revenue
from sales
join product
using (product_id)
group by 1,2)



select user_id, product_id
from t
join
(select user_id, max(revenue) as revenue
from t
group by user_id) as x
using (user_id, revenue)
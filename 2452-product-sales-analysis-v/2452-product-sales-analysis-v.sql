# Write your MySQL query statement below
select user_id, sum(quantity*price) as spending
from sales
join product
using (product_id)
group by 1
order by 2 DESC, 1 ASC
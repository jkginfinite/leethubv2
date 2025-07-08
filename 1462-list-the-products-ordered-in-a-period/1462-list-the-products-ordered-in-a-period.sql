# Write your MySQL query statement below
select product_name, sum(unit) as unit
from products
join orders
using (product_id)
where order_date like '2020-02%'
group by 1
having sum(unit)>=100
# Write your MySQL query statement below
with cte as
(select product_id, year(purchase_date) cy,
lead(year(purchase_date)) over (partition by product_id order by year(purchase_date)) ny
from orders
group by 1,2
having count(*)>2
)

select distinct product_id
from cte
where cy+1=ny
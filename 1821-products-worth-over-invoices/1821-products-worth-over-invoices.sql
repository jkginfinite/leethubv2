# Write your MySQL query statement below
select name, ifnull(sum(rest),0) as rest, ifnull(sum(paid),0) as paid, ifnull(sum(canceled),0) as canceled, ifnull(sum(refunded),0) as refunded
from product
left join invoice
using (product_id)
group by name
order by name
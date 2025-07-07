# Write your MySQL query statement below
select seller_name
from orders
right join seller
using (seller_id)
where seller_id not in (select seller_id from orders where sale_date like '2020%')
order by seller_name ASC
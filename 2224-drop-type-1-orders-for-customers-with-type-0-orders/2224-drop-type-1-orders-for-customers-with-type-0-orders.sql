# Write your MySQL query statement below
select order_id, customer_id, order_type
from
(select order_id, customer_id,
case when
customer_id in (select customer_id from orders where order_type=0) and order_type=1 then null
else order_type
end as order_type
from orders) as X
where order_type is not null
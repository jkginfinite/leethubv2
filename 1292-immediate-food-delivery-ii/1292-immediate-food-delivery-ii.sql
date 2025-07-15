# Write your MySQL query statement below
with t as
(select customer_id, min(order_date) as first_order
from delivery
group by 1),


t2 as
(select delivery_id, customer_id, case when order_date=customer_pref_delivery_date then 1 else 0
end as immediate,
case when order_date=first_order then 1 else 0 end as initial
from delivery
join t
using (customer_id))

select round(100*sum(immediate)/sum(initial),2) as immediate_percentage
from t2
where initial=1

# Write your MySQL query statement below
with t1 as
(select order_date,
case when customer_pref_delivery_date=order_date then 'immediate'
else 'scheduled'
end as type
from delivery),

t2 as
(select order_date, count(*) as tot
from t1
group by 1),

t3 as
(select order_date, type, count(*) as tot1
from t1
group by 1,2),

t4 as
(select order_date, round(ifnull(100*tot1/tot,0),2) as immediate_percentage
from t2
inner join t3
using (order_date)
where type='immediate')

select order_date, ifnull(immediate_percentage,0) as immediate_percentage
from t4
right join 
(select distinct order_date
from delivery) as x
using (order_date)
order by 1 ASC
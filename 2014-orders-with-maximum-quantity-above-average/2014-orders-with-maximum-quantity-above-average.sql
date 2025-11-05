# Write your MySQL query statement below
with t1 as
(select order_id, max(quantity) as maxx, avg(quantity) as mean2
from OrdersDetails
group by 1),

t2 as
(select max(mean2) as maxxmean2
from t1)

select distinct order_id
from ordersdetails
join t1
using (order_id)
join t2
where maxx>maxxmean2
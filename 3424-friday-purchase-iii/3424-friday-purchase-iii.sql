# Write your MySQL query statement below
with t as
(select A.membership, B.*, week(B.purchase_date) -44 +1 as week_of_month
from users A
right join purchases B
using (user_id)
where B.purchase_date>'2023-10-31' and B.purchase_date<'2023-12-01' and DAYOFWEEK(B.purchase_date)=6),

t2 as
(select week_of_month, membership, sum(amount_spend) as total_amount
from t
group by 1,2),


wkn as
(select 1 week_of_month
union all 
select 2
union all
select 3
union all
select 4),

mbr as
(select 'Premium' membership
union all
select 'VIP')

select week_of_month, membership, ifnull(total_amount,0) as total_amount
from wkn
cross join mbr
left join t2
using (week_of_month, membership)
where membership!='Standard'
order by 1 ASC, 2 ASC
# Write your MySQL query statement below
with t1 as
(select DATE_FORMAT(trans_date, "%Y-%m") as month, IFNULL(country,'x') as country,  count(id) as trans_count,
sum(amount) as trans_total_amount
from transactions
group by 1,2),

t2 as
(select DATE_FORMAT(trans_date,"%Y-%m") as month, IFNULL(country,'x') as country, count(id) as approved_count,
sum(amount) as approved_total_amount
from transactions
where state='approved'
group by 1,2)


select month, 
case when country='x' then null else country end as country, 
IFNULL(trans_count,0) as trans_count, 
IFNULL(approved_count,0) as approved_count, 
IFNULL(trans_total_amount,0) as trans_total_amount, 
IFNULL(approved_total_amount,0) as approved_total_amount
from t1
left join t2
using (month,country)
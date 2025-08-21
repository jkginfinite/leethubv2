# Write your MySQL query statement below
with t as
(select country, date_format(trans_date, '%Y-%m') as dt, count(*) as approved_count,
sum(amount) as approved_amount
from transactions as t
where state='approved'
group by dt, country),

t1 as
(select country,
date_format(c.trans_date, '%Y-%m') as dt,
count(*) as chargeback_count,
sum(amount) as chargeback_amount
from chargebacks as c
join transactions as t
on c.trans_id = t.id
group by dt, country),

t2 as
(select dt,country 
from t
union
select dt,country
from t1)

select t2.dt as month,
t2.country,
ifnull(approved_count,0) as approved_count,
ifnull(approved_amount,0) as approved_amount,
ifnull(chargeback_count,0) as chargeback_count,
ifnull(chargeback_amount,0) as chargeback_amount
from t2
left join t
on t2.dt = t.dt
and t2.country = t.country
left join t1
on t2.dt = t1.dt
and t2.country = t1.country
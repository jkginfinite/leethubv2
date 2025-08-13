# Write your MySQL query statement below
with t1 as
(select account_id, day,
CASE WHEN type='Withdraw' then -1*amount else amount end as amount1,
--RANK() OVER (partition by account_id ORDER BY DAY ASC) as rnk
from transactions)

select account_id, day, SUM(amount1) OVER (partition by account_id ORDER BY DAY asc) as balance
from t1
group by 1,2
order by 1 ASC, 2 ASC
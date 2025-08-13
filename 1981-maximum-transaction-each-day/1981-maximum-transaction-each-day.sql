# Write your MySQL query statement below
with t as
(select day, max(amount) as amount
from transactions
group by 1)

select distinct(transaction_id) as transaction_id
from t
left join transactions
using (day,amount)
order by 1 ASC
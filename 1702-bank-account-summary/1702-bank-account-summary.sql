# Write your MySQL query statement below
/*select user_id,user_name,credit,
case when paid_by=user_id then -1*amount

from transactions
left join users
on users.user_id = transactions.paid_by
group by 1,2,3*/
with t as
(select B.*, -A.amount as amount
from transactions A
right join users B
on B.user_id = A.paid_by

union all

select C.*, D.amount as amount
from transactions D
right join users C
on C.user_id = D.paid_to)


select user_id, user_name, credit+total_amount as credit, 
case when credit+total_amount<=0 then 'Yes'
else 'No'
end as credit_limit_breached
from
(select user_id, user_name, credit, ifnull(sum(amount),0) as total_amount
from t
group by 1,2,3) as x

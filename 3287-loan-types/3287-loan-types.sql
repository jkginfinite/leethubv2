# Write your MySQL query statement below
with t1 as
(select user_id
from loans
where loan_type='Mortgage'
group by 1
having count(loan_type)>=1),
t2 as
(select user_id
from loans
where loan_type='Refinance'
group by 1
having count(loan_type)>=1)

select distinct(user_id) as user_id
from loans
where user_id in (select * from t1) and user_id in (select * from t2)
order by 1 ASC
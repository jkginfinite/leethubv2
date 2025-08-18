# Write your MySQL query statement below
with t as
(select dep_id, count(emp_id) as c
from employees
group by 1
order by 2 DESC)

select emp_name as manager_name, dep_id
from employees
where dep_id in (select dep_id from t where c in (select max(c) from t))
and position='Manager'
order by 2 ASC
# Write your MySQL query statement below
with t1 as
(select employee_id
from employees
where employee_id in (select employee_id from employees where manager_id=1 and employee_id!=1)),

t2 as
(select employee_id
from employees
where manager_id in (select * from t1))


select employee_id
from employees
where manager_id in (select * from t2)

union all

select *
from t2

union all

select *
from t1
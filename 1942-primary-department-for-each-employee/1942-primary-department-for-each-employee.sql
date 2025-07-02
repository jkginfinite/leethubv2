# Write your MySQL query statement below

with t1 as
(select employee_id, department_id
from employee
where primary_flag='Y'),

t2 as
(select employee_id, department_id
from employee
where employee_id in (select employee_id from employee group by employee_id having count(department_id)=1))

select *
from t1
union all
select *
from t2
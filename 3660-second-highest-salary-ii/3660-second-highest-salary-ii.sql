# Write your MySQL query statement below
select emp_id, dept
from
(select emp_id, dept, dense_rank() over (partition by dept order by salary DESC) as r
from employees
order by emp_id ASC) as x
where r=2

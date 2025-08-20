# Write your MySQL query statement below
with t1 as
(select company_id, max(salary) as max_salary
from salaries
group by 1)

select company_id, employee_id, employee_name, round(salary*tax) as salary
from 
(select *,
case when max_salary between 1000 and 10000 then 1-0.24
when max_salary>10000 then 1-0.49
else 1
end as tax
from salaries
join t1
using (company_id)) as x
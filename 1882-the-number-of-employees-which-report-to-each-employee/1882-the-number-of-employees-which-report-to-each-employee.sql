# Write your MySQL query statement below
with t1 as
(select reports_to, count(employee_id) as reports_count, round(avg(age)) as average_age
from employees
where reports_to is not null
group by 1)


select A.employee_id, A.name, B.reports_count, B.average_age
from employees A
join t1 B
on A.employee_id = B.reports_to
order by 1 ASC
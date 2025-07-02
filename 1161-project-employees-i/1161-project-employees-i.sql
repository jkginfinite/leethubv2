# Write your MySQL query statement below
select A.project_id, round(avg(experience_years),2) as average_years
from project A
join employee B
using (employee_id)
group by 1
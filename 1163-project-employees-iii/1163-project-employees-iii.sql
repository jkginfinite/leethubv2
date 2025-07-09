# Write your MySQL query statement below
with t1 as
(select project_id, employee_id, experience_years
from project
join employee
using (employee_id))


select project_id, employee_id
from t1
join
(select project_id, max(experience_years) as experience_years
from t1
group by project_id) as X
using (project_id, experience_years)
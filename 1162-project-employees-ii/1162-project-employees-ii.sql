# Write your MySQL query statement below
with t as
(select project_id, count(distinct employee_id) as c
from project
group by 1
order by 2 DESC)

select project_id 
from t
where c=(select max(c) from t)
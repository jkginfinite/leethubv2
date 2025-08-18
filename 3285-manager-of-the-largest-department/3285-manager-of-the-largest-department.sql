# Write your MySQL query statement below
with cte as
(select *, case when position='Manager' then COUNT(emp_id) ELSE 0 END AS COUNT
FROM employees
GROUP BY dep_id),

cte1 as
(SELECT *, RANK() OVER (ORDER by count DESC) rnk
from cte)

select emp_name as manager_name, dep_id
from cte1
where rnk=1
order by dep_id
with t as
(select department, max(salary) as salary
from salaries
where department in ('Marketing','Engineering')
group by 1)

select max(salary)-min(salary) as salary_difference
from t


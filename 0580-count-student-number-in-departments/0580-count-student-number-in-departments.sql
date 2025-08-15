# Write your MySQL query statement below
with t1 as
(select *
from department A
left join student B
using (dept_id))

select dept_name, count(student_id) as student_number
from t1
group by 1
order by 2 DESC, 1 ASC
/*union

select dept_name, 0 as student_number
from t1
where student_id is null*/
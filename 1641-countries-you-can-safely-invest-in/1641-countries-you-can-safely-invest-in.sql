# Write your MySQL query statement below
with t1 as
(select *, CAST(SUBSTRING_INDEX(phone_number, '-', 1) AS UNSIGNED) as country_code
from person A
join calls B
on A.id = B.caller_id or A.id = B.callee_id)

select distinct name as country from
(select country_code, B.name, avg(duration) as avg_duration
from t1 A
join country B
using (country_code)
group by 1,2
having avg(duration)>(select avg(duration) from t1))
as x
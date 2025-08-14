# Write your MySQL query statement below
with t1 as
(select city_id, max(degree) as degree
from weather
group by city_id)

select city_id, min(day) as day, degree
from weather
join t1
using (city_id,degree)
group by city_id, degree
order by city_id ASC
# Write your MySQL query statement below

with t1 as
(select state
from cities
group by state
having count(city)>=3),

t2 as
(select state
from cities
group by state
having SUM(CASE WHEN LEFT(city,1)=LEFT(STATE,1) then 1 else 0 end)>=1)

select state, group_concat(city ORDER BY city SEPARATOR ', ') as cities, SUM(CASE WHEN LEFT(city,1)=LEFT(STATE,1) then 1 else 0 end) as matching_letter_count
from cities
where state in (select state from t1) and state in (select state from t2)
group by 1
order by 3 DESC, 1 ASC

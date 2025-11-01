# Write your MySQL query statement below
with t as
(select airport_id, sum(flights_count) as cnt
from
(select departure_airport as airport_id, flights_count
from flights
union all
select arrival_airport as airport_id, flights_count
from flights) as x
group by 1)


select airport_id
from t
join
(select max(cnt) as cnt
from t) as x
using (cnt)

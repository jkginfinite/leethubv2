# Write your MySQL query statement below
with t1 as
(select event_type, avg(occurrences) as avg_occurrences
from events
group by 1)


select business_id
from events A
join t1 B
using (event_type)
where A.occurrences>B.avg_occurrences
group by 1
having count(business_id)>1
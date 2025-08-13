# Write your MySQL query statement below
with t1 as
(select log_id,
log_id - RANK() OVER (ORDER BY log_id ASC) as r1
from Logs)


select min(log_id) as start_id, max(log_id) as end_id
from
(select *,
RANK() over (order by r1 ASC) as r2
from t1) as x
group by r2
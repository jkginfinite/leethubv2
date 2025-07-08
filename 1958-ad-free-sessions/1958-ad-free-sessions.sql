# Write your MySQL query statement below
select session_id
from playback a
left join ads b
on a.customer_id = b.customer_id
and timestamp between start_time and end_time
where ad_id is null
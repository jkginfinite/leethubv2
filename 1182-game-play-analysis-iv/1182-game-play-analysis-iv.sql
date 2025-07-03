# Write your MySQL query statement below
with t1 as
(select player_id, first_date, DATE_ADD(first_date, INTERVAL 1 DAY) as day_after_first
from
(select player_id, min(event_date) as first_date
from activity
group by 1) as X)


select round(count(*)/(select count(distinct player_id) from activity),2) as fraction
from t1
join activity
on t1.player_id = activity.player_id and t1.day_after_first=activity.event_date
# Write your MySQL query statement below
with paid as
(select user_id, activity_type, round(sum(activity_duration)/count(activity_duration),2) as paid_avg_duration
from useractivity
where user_id in (select distinct user_id from useractivity where activity_type='paid') and activity_type='paid'
group by 1,2),

trial as
(select user_id, activity_type, round(sum(activity_duration)/count(activity_duration),2) as trial_avg_duration
from useractivity
where user_id in (select distinct user_id from useractivity where activity_type='paid') and activity_type='free_trial'
group by 1,2)

select user_id, A.trial_avg_duration, B.paid_avg_duration
from trial A
join paid B
using (user_id)
order by 1 ASC
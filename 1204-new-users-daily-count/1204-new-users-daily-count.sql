# Write your MySQL query statement below
with t1 as
(select user_id, min(activity_date) as activity_date
from traffic
where activity='login'
group by 1)

select activity_date as login_date, count(user_id) as user_count
from t1
where activity_date>=DATE_ADD('2019-06-30', INTERVAL -90 DAY)
group by 1
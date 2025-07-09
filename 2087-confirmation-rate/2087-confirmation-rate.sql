# Write your MySQL query statement below
with t1 as
(select A.user_id, A.time_stamp as time_stamp1, B.time_stamp as time_stamp2, B.action
from signups A
left join confirmations B
using (user_id)),

t3 as
(select user_id, count(time_stamp1) as requested
from t1
group by 1),

t4 as
(select user_id, count(time_stamp2) as confirmed
from t1
where action='confirmed'
group by 1)

select user_id, ifnull(round(confirmed/requested,2),0) as confirmation_rate
from t3
left join t4
using (user_id)
# Write your MySQL query statement below
with cte as(
    select user_id ,count(distinct session_id) rnk 
    from Activity 
    where activity_date between '2019-06-28' and '2019-07-27'
    group by 1
)
select  round(ifnull(avg(rnk),0),2) as average_sessions_per_user 
from cte
# Write your MySQL query statement below
/*select user_id, count(post_id)/7 OVER (partition by user_id,week(post_date) order by post_date ASC) as avg_weekly_posts,
count(post_id) OVER (partition by user_id,week(post_date) order by post_date ASC) as avg_weekly_posts
from posts
where post_date>='2024-02-01' and post_date<='2024-02-28'
group by user_id*/

with cte as
(
    SELECT *, count(*) over (partition by user_id)/4 as avg_weekly_posts
    from posts
    where post_date between '2024-02-01' and '2024-02-28' 
),

cte2 AS 
(
    SELECT *, count(post_id) over (partition by user_id order by post_date range between interval 6 day preceding and current row) as max_7day_posts
    from cte
)

select distinct user_id, max(max_7day_posts) as max_7day_posts, avg_weekly_posts
from cte2
where max_7day_posts >= 2*avg_weekly_posts
group by 1
order by 1
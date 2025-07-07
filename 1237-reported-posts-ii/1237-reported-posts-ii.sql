# Write your MySQL query statement below
SELECT ROUND(AVG(daily_rate)*100,2) AS average_daily_percent
FROM (
select action_date,
count(distinct case when a.post_id=r.post_id then r.post_id END)/count(distinct a.post_id) AS daily_rate
FROM Actions a
LEFT JOIN Removals r
on a.post_id = r.post_id
WHERE a.extra = 'spam'
GROUP BY action_date) x
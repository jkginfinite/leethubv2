with cte as (
SELECT '[0-5>' AS bin, 0 as min_duration, 5*60 as max_duration
UNION ALL
SELECT '[5-10>' as bin, 5*60 as min_duration, 10*60 as max_duration
UNION ALL
SELECT '[10-15>' as bin, 10*60 as min_duration, 15*60 as max_duration
UNION ALL
SELECT '15 or more' as bin, 15*60 as min_duration, 2147483647 as max_duration
)

select cte.bin, count(s.session_id) as total
FROM sessions s
RIGHT JOIN cte on s.duration>=min_duration and s.duration<max_duration
GROUP BY cte.bin;
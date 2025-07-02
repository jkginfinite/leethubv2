# Write your MySQL query statement below
with t1 as
(select query_name, round(avg(rating/position),2) as quality
from queries
group by 1),
t2 as
(select query_name, count(*) as poor_query
from queries
where rating<3
group by 1),
t3 as
(select query_name, count(*) as total_query
from queries
group by 1)

select query_name, quality, ifnull(round(100*poor_query/total_query,2),0) as poor_query_percentage
from t1
left join t2
using (query_name)
left join t3
using (query_name)

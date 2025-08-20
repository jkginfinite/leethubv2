# Write your MySQL query statement below
with t1 as
(select A.id, A.activity
from friends A
join activities B
on A.activity = B.name),

t2 as
(select activity, count(id) as cnt
from t1
group by 1)


select activity
from t2
where cnt<(select max(cnt) from t2) and cnt>(select min(cnt) from t2)
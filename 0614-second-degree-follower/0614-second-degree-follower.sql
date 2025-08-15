# Write your MySQL query statement below
with t1 as
(select followee as f, count(follower) as c1
from follow
group by 1
having count(follower)>=1),

t2 as
(select follower as f, count(followee) as c2
from follow
group by 1
having count(followee)>=1)


select f as follower, c1 as num
from t1
join t2
using (f)
order by f ASC, num DESC
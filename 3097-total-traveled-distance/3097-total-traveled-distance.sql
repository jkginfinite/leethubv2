# Write your MySQL query statement below
select user_id, name, sum(distance) as `traveled distance`
from
(select user_id, name, IFNULL(ride_id,0) as ride, IFNULL(distance,0) as distance
from users
left join rides
using (user_id)) x
group by 1,2
order by 1 ASC
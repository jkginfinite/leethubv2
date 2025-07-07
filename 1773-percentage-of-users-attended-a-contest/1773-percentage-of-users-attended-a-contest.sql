# Write your MySQL query statement below
select contest_id, round(100*count(user_id)/(select count(user_id) from users),2) as percentage
from register
group by 1
order by 2 DESC, 1 ASC
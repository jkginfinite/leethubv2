# Write your MySQL query statement below
with t as
(select user1_id, user2_id, count(*) as cnt
from
(select A.user_id as user1_id, B.user_id as user2_id
from relations A
cross join relations B
on A.user_id<B.user_id and A.follower_id=B.follower_id) as x
group by 1,2)


select user1_id, user2_id
from t
where cnt= (select max(cnt) from t)
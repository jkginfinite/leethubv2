# Write your MySQL query statement below

with t1 as(
    select user1_id users, user2_id as friends
    from friendship
    union all
    select user2_id users, user1_id as friends
    from friendship
)

select f.user1_id, f.user2_id, count(t1.friends) as common_friend
from friendship as f
join t1
on f.user1_id=t1.users
join t1 fb
on f.user2_id=fb.users
and t1.friends=fb.friends
group by f.user1_id, f.user2_id
having count(*)>2
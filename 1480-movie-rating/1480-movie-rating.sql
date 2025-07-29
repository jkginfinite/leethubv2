# Write your MySQL query statement below
with t as
(select *
from movierating
join users 
using (user_id)
join movies
using (movie_id)),

t2 as
(select user_id, name, count(rating) as c
from t
group by 1,2
order by c DESC),

t3 as
(select user_id, name, RANK() over (order by name ASC) as r
from t2
where c=(select max(c) from t2)),

/*select name
from t3
where r=1*/

t4 as
(select title, avg(rating) as r
from t
where created_at>='2020-02-01' and created_at<'2020-03-01'
group by 1
order by 2 DESC),

t5 as
(select title, RANK() over (order by title ASC) as r
from t4
where r = (select max(r) from t4))


select name as results
from t3
where r=1
union all
select title as results
from t5
where r=1
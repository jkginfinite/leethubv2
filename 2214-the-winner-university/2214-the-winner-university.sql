# Write your MySQL query statement below

with ny as
(select count(student_id) as c1, "New York University" as school1
from newyork
where score>=90),

ca as
(select count(student_id) as c2, "California University" as school2
from california
where score>=90)

select case when c1>c2 then school1
when c2>c1 then school2
else "No Winner"
end as winner
from ny
cross join ca
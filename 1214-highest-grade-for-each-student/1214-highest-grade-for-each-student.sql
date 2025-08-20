# Write your MySQL query statement below
with t as
(select student_id, max(grade) as grade
from enrollments
group by student_id)


select student_id, min(course_id) as course_id, grade
from enrollments
join t
using (student_id,grade)
group by student_id, grade
order by student_id ASC
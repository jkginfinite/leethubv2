# Write your MySQL query statement below
select A.student_name as member_A, 
B.student_name as member_B, 
C.student_name as member_C
from schoolA as A
cross join schoolB as B
cross join schoolC as C
where A.student_id!=B.student_id and A.student_id!=C.student_id and B.student_id!=C.student_id
and A.student_name!=B.student_name and C.student_name!=B.student_name and  A.student_name!=C.student_name
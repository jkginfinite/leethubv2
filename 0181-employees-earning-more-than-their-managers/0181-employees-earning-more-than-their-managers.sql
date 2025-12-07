# Write your MySQL query statement below

select A.name as employee
from employee A
join employee B
on A.managerId = B.id
where A.salary>B.salary
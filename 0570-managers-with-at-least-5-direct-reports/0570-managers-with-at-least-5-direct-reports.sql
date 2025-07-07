# Write your MySQL query statement below
select name
from employee
where id in
(select managerId from (select managerId, count(distinct id)
from employee
group by managerId
having count(distinct id)>=5) as x)
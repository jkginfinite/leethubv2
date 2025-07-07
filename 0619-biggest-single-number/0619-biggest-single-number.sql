# Write your MySQL query statement below
select max(num) as num
from
(select num, count(num)
from mynumbers
group by 1
having count(num)=1) X
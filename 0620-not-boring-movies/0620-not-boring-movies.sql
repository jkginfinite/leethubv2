# Write your MySQL query statement below
select *
from cinema
where description!='boring' and MOD(id,2)!=0
order by rating DESC

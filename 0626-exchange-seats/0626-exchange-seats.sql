# Write your MySQL query statement below
with evens as
(select id-1 as id, student
from seat A
where MOD(id,2)=0),
odds as
(select id+1 as id, student
from seat B
where MOD(id,2)!=0)


select 
case when MOD((select count(*) from seat),2)!=0 and id-1=(select count(*) from seat) then
id-1 else id
end as id,
student
from odds
union all
select *
from evens
order by id ASC
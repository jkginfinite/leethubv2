# Write your MySQL query statement below
select N,
CASE when P is null then 'Root'
WHEN N NOT IN (SELECT P FROM tree where P is not null) THEN 'Leaf'
else 'Inner'
end as Type
from Tree
order by N ASC

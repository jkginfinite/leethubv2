# Write your MySQL query statement below
select person_id, concat(name,'(',upper(LEFT(profession,1)),')') as name
from person
order by 1 DESC
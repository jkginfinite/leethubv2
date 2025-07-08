# Write your MySQL query statement below
select artist, count(*) as occurrences
from spotify
group by 1
order by 2 DESC, 1 ASC
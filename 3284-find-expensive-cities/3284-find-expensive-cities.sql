# Write your MySQL query statement below

#strategy: find national avg home price
# then
select city 
from
(select city, avg(price) avg_price
from listings
group by 1) X
where avg_price>(select avg(price) from listings)
order by 1 ASC
# Write your MySQL query statement below
with first_year as
(select product_id, min(year) as year
from sales
group by 1)

select product_id, year as first_year, quantity, price
from sales
join first_year
using (product_id, year)
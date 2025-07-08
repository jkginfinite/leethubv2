# Write your MySQL query statement below
select lower(REPLACE(product_name, ' ', '')) as product_name, LEFT(sale_date,7) as sale_date, count(sale_id) as total
from sales
group by 1,2
ORDER BY 1 ASC, 2 ASC
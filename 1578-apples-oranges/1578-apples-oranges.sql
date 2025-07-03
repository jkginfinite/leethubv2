# Write your MySQL query statement below
with t1 as
(select sale_date, sold_num
from sales as y
where fruit='apples'),
t2 as
(select sale_date, sold_num
from sales
where fruit='oranges')

select sale_date, Y.sold_num-X.sold_num as diff
from t1 as Y
join t2 as X
using (sale_date)

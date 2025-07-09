# Write your MySQL query statement below
with t1 as
(select product_id, max(change_date) as change_date
from products
where change_date<='2019-08-16'
group by 1)

select product_id, price 
FROM
(select product_id, IFNULL(new_price,10) as price, IFNULL(change_date, '2019-08-16') as change_date
from (select distinct product_id from products) as x
left join t1
using (product_id)
left join products
using (product_id,change_date)) as X
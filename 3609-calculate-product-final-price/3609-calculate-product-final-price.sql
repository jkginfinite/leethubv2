# Write your MySQL query statement below
select product_id, 
case when discount is not null
then (1-discount/100)*price
else price
end as final_price,
category
from products
left join discounts
using (category)
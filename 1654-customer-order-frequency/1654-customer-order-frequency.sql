select customer_id, name
from customers
join orders
using (customer_id)
join product
using (product_id)
where YEAR(order_date)=2020
group by customer_id
HAVING sum(IF(MONTH(order_date)=6,quantity,0)*price)>=100 AND SUM(IF(MONTH(order_date)=7,quantity,0)*price)>=100
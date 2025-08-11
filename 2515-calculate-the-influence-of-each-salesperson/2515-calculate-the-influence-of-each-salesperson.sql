# Write your MySQL query statement below
with t as
(select salesperson_id, name, price
from salesperson
left join customer
using (salesperson_id)
left join sales
using (customer_id))


select salesperson_id, name, ifnull(sum(price), 0) as total
from t
group by salesperson_id, name;


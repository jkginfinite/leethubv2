# Write your MySQL query statement below
/*select A.*, B.operation_day, B.price
from stocks A
join stocks B
on A.stock_name = B.stock_name and A.operation!=B.operation and A.operation_day<B.operation_day
where A.operation='Buy' and B.operation='Sell' and A.stock_name='Corona Masks'
order by A.stock_name ASC*/

select stock_name, sum(capital) as capital_gain_loss
from
(select stock_name, case when operation='Sell' then price else -1*price end as capital
from stocks) as x
group by 1
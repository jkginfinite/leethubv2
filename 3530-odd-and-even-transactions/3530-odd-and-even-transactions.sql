# Write your MySQL query statement below
select transaction_date, ifnull(sum(odd),0) as odd_sum, ifnull(sum(even),0) as even_sum
from
(select transaction_date, 
case when MOD(amount,2)=0 then amount
end as even,
case when MOD(amount,2)!=0 then amount
end as odd
from transactions)
as x
group by 1
order by 1 ASC
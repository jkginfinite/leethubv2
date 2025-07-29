# Write your MySQL query statement below
with t as
(select YEAR(transaction_date) as year, product_id, sum(spend) as spend
from user_transactions
group by 1,2)


select A.year, A.product_id, A.spend as curr_year_spend, B.spend as prev_year_spend, round(100*(A.spend-B.spend)/B.spend,2) as yoy_rate
from t as A
left join t as B
on B.year+1 = A.year and A.product_id=B.product_id
order by A.product_id,A.year ASC
# Write your MySQL query statement below
select count(distinct customer_id) as rich_count from store where amount>500
#having count(bill_id)>=1 and

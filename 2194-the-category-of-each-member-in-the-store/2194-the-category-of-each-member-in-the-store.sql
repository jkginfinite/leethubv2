# Write your MySQL query statement below
with t as
(select member_id, name, visit_id, visit_date, charged_amount
from visits
left join purchases
using (visit_id)
right join members
using (member_id)),

t2 as
(select member_id, count(charged_amount) as total_purchases, count(visit_id) as total_visits
from t
group by 1)


select distinct member_id, name,
case 
when 100*total_purchases/total_visits>=80 then 'Diamond'
when 100*total_purchases/total_visits>=50 and 100*total_purchases/total_visits<80 then 'Gold'
when 100*total_purchases/total_visits<50 and total_visits>0 then 'Silver'
when total_visits=0 then 'Bronze'
end as category
from t
left join t2
using (member_id)

# Write your MySQL query statement below
select user_id
from emails
join texts
using (email_id)
where signup_action='Verified' and DATEDIFF(action_date,signup_date)=1
order by 1 ASC
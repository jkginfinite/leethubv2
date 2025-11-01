# Write your MySQL query statement below
select count(distinct account_id) as accounts_count
from subscriptions A
left join streams B
using (account_id)
where (A.start_date like '2021%' or A.end_date like '2021%') and stream_date not like '2021%'
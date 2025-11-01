# Write your MySQL query statement below
select distinct a.account_id
from loginfo a
cross join loginfo b
where a.login<=b.logout and b.login<=a.logout and a.account_id = b.account_id and a.ip_address!=b.ip_address
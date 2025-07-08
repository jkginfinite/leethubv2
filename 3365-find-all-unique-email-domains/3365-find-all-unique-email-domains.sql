# Write your MySQL query statement below
select SUBSTRING_INDEX(email,'@',-1) AS email_domain, count(*) as count
from emails
where email like '%.com'
group by 1
order by 1 ASC
# Write your MySQL query statement below
select *
from users
where REGEXP_LIKE(email,'^[A-Za-z0-9_]+@[A-Za-z]+\\.com')
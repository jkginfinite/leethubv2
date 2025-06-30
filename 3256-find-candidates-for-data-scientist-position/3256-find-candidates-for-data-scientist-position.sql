# Write your MySQL query statement below
with t as
(select candidate_id, JSON_ARRAYAGG(skill) as skill
from candidates
group by 1
order by 1 ASC)


select candidate_id
from t
where JSON_CONTAINS(skill,'["Python","Tableau","PostgreSQL"]')
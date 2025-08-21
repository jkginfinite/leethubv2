# Write your MySQL query statement below
with t as
(select distinct *
from views)

select distinct A.viewer_id as id
from t A
join t B
on A.view_date = B.view_date and A.article_id!=B.article_id and A.viewer_id = B.viewer_id
order by 1 ASC
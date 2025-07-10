# Write your MySQL query statement below
select distinct title as title
from tvprogram
join content
using (content_id)
where program_date like '2020-06%' and kids_content='Y' and content_type='Movies'
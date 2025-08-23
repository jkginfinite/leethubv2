# Write your MySQL query statement below
with candidate_info as
(select candidate_id, project_id, count(skill) as skills,
100+sum(case when proficiency>importance then 10 when proficiency<importance then -5 else 0 end) score
from candidates
join projects
using (skill)
group by 1,2),

project_info as
(select project_id, count(skill) as skills
from projects
group by 1),

cte as (
    select project_id, candidate_id, score,
    dense_rank() over (partition by project_id order by score DESC, candidate_id) rnk
    from candidate_info
    join project_info
    using (skills, project_id)
)

select project_id, candidate_id, score
from cte
where rnk=1
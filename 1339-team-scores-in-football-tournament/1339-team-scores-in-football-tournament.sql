# Write your MySQL query statement below
with t as
(select 
B.team_name as host_name,
C.team_name as guest_name,
CASE 
    WHEN A.host_goals = A.guest_goals then 'draw'
    WHEN A.host_goals > A.guest_Goals then B.team_name
    ELSE C.team_name
END AS winner,
CASE 
    WHEN A.host_goals = A.guest_goals then 1
    ELSE 3
END AS points
FROM matches A
JOIN teams B on A.host_team = B.team_id
JOIN teams C on A.guest_team = C.team_id),

t2 as
(select winner, sum(points) as points
from t
where winner!='draw'
group by 1),

t3 as
(select team_name, sum(points) as points
from
(select host_name as team_name, points
from t
where winner='draw'
union all
select guest_name as team_name, points
from t
where winner='draw'
union all
select *
from t2) as x
group by 1)

select team_id, team_name, ifnull(points,0) as num_points
from teams
left join t3
using (team_name)
order by num_points DESC, team_id ASC
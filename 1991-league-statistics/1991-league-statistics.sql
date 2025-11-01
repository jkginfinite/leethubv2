# Write your MySQL query statement below
with matches1 as
(select *, 
case when home_team_goals>away_team_goals
then 3
when home_team_goals=away_team_goals
then 1
else 0
end as home_team_points,
case when home_team_goals<away_team_goals
then 3
when home_team_goals=away_team_goals
then 1
else 0
end as away_team_points
from matches),

home as
(select home_team_id as team_id, count(*) as matches, sum(home_team_goals) as goals_for, sum(away_team_goals) as goals_against,
sum(home_team_points) as points
from matches1
group by 1),
away as
(select away_team_id as team_id, count(*) as matches, sum(away_team_goals) as goals_for, sum(home_team_goals) as goals_against,
sum(away_team_points) as points
from matches1
group by 1),

results as
(select team_id, sum(matches) as matches_played, sum(points) as points, sum(goals_for) as goal_for, sum(goals_against) as goal_against,
sum(goals_for)-sum(goals_against) as goal_diff
from
(select *
from home
union all
select *
from away) as x
group by team_id)


select team_name, matches_played, points, goal_for, goal_against, goal_diff
from
(select A.team_name, B.*
from teams A
inner join results B
using (team_id)
order by points DESC, goal_diff DESC, team_name ASC)
as x
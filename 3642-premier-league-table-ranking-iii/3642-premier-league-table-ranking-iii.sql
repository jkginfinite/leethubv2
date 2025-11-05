with cte as
(select season_id, team_id, team_name,
wins*3+draws as points,
goals_for - goals_against as goal_difference
from seasonstats)


select *,
dense_rank() over (partition by season_id order by points DESC, goal_difference DESC, team_name) as position
from cte
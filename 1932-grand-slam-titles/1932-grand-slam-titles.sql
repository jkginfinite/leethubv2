# Write your MySQL query statement below
/*select *,
Case when player_id=wim
from players A
join championships B
on A.player_id = B.Fr_open or A.player_id = B.US_open or A.player_id = B.Au_open or A.player_id = B.Wimbledon
where player_id = wimbledon or player_id = Fr_open or player_id=US_open or player_id = Au_open
order by player_id, player_name ASC
group by player_id, player_name*/


SELECT player_id,player_name,
SUM(player_id=Wimbledon)+SUM(player_id=Fr_open)+SUM(player_id=us_open)+SUM(player_id=au_open)
as grand_slams_count
FROM players
JOIN championships
ON player_id=Wimbledon or player_id=Fr_open or player_id=US_open or player_id=Au_open
GROUP BY 1,2
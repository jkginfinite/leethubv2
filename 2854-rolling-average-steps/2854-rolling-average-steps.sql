select A.user_id, A.steps_date, round((A.steps_count+B.steps_count+C.steps_count)/3,2) as rolling_average
from steps A
join steps B
on DATE_SUB(A.steps_date, INTERVAL 1 DAY) = B.steps_date and A.user_id = B.user_id
join steps c
ON DATE_SUB(A.steps_date, INTERVAL 2 DAY) = C.steps_date and A.user_id = C.user_id
order by 1 ASC, 2 ASC
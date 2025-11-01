
with t1 as
(SELECT
  user_id,
  visit_date,
  RANK() OVER (PARTITION BY user_id ORDER BY visit_date ASC) AS ranking
FROM uservisits)

select user_id, max(diff) as biggest_window
from
(select A.user_id, DATEDIFF(ifnull(b.visit_date,'2021-1-1'),a.visit_date) as diff
from t1 a
left join t1 b
on a.user_id = b.user_id and a.ranking = b.ranking-1) as x
group by 1
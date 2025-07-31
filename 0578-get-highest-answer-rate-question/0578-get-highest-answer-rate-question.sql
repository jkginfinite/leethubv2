# Write your MySQL query statement below
with t1 as
(select question_id, count(action) as c1
from SurveyLog
where action='show'
group by 1),

t2 as
(select question_id, count(action) as c2
from SurveyLog
where action='answer'
group by 1)

select survey_log
from 
(select question_id as survey_log, c2/c1 as rate, RANK() over (order by c2/c1 DESC) as r
from t1
join t2
using (question_id)
order by 1 ASC, 3 DESC) as x
where r=1
limit 1
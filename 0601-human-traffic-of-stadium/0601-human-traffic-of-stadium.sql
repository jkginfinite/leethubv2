# Write your MySQL query statement below
with stadium_with_rnk as
(select
id, visit_date, people, rnk, (id-rnk) as island
FROM (
    select id, visit_date, people, RANK() OVER (order by id) as rnk
    FROM stadium
    WHERE people>=100
) as t0)

SELECT id, visit_date, people
FROM stadium_with_rnk
where island IN (SELECT island FROM stadium_with_rnk GROUP BY island HAVING COUNT(*)>=3)
order by visit_date
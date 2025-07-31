# Write your MySQL query statement below
with t as
(select alpha.x as x1, alpha.y as y1, beta.x as x2, beta.y as y2
from Point2D as alpha
cross join Point2D as beta)

select min(shortest) as shortest
from
(select round(Power((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2),0.5),2) as shortest
from t
where Power((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2),0.5)>0) as x
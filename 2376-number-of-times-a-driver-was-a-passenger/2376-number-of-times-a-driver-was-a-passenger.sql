# Write your MySQL query statement below
select A.driver_id, count(distinct B.ride_id) as cnt
from rides A
left join rides B
on A.driver_id = B.passenger_id
group by 1
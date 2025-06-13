# Write your MySQL query statement below
with t as
(select A.country_name,avg(B.weather_state) as avg_weather
from countries A
join weather B
using (country_id)
where B.day>="2019-11-01" and B.day<"2019-12-01"
group by 1)

select country_name, 
case when avg_weather<=15 then "Cold"
when avg_weather>=25 then "Hot"
else "Warm"
end as weather_type
from t
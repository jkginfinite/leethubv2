select co.name as country
from person p
join country co
ON SUBSTRING(phone_number,1,3)=country_code
JOIN calls c
ON p.id IN (c.caller_id, c.callee_id)
group by co.name
HAVING AVG(duration)>(SELECT AVG(duration) from calls)
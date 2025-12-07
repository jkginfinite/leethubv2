select a.employee_id, count(*) as overlapping_shifts
from employeeshifts A
inner join employeeshifts B
on a.employee_id = b.employee_id and a.start_time<b.start_time and a.end_time>b.start_time
group by 1
order by 1 ASC
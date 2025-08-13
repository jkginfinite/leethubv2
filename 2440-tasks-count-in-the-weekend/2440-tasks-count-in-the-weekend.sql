SELECT SUM(weekday(submit_date)>=5) as weekend_cnt,
SUM(weekday(submit_date)<5) as working_cnt
FROM tasks
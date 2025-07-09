select distinct(A.user_id) as user_id
from confirmations A
join confirmations B
on A.user_id = B.user_id and A.time_stamp<B.time_stamp
where TIMESTAMPDIFF(SECOND,A.time_stamp,B.time_stamp)<=60*60*24
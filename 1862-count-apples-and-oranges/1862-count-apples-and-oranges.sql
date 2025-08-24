# Write your MySQL query statement below
select sum(A.apple_count+ifnull(B.apple_count,0)) as apple_count, 
sum(A.orange_count+ifnull(B.orange_count,0)) as orange_count
from boxes A
left join chests B
using (chest_id)
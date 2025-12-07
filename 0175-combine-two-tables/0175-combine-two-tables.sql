# Write your MySQL query statement below
select firstName, lastName, city, state
from address A
right join person P
using (personID)
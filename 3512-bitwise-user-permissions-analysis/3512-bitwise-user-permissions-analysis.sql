# Write your MySQL query statement below
select BIT_AND(permissions) as common_perms, BIT_OR(permissions) as any_perms
from user_permissions
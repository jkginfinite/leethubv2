SELECT 'Low Salary' as category,
SUM(CASE WHEN income<20000 then 1 else 0 end) as accounts_count
from accounts

union 

SELECT 'Average Salary' as category,
SUM(CASE WHEN income>=20000 AND income<=50000 THEN 1 else 0 end)
AS accounts_count
FROM accounts

UNION

SELECT 'High Salary' as category,
SUM(CASE WHEN income>50000 then 1 else 0 end) as accounts_count
FROM accounts
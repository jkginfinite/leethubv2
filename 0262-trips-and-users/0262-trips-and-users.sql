# Write your MySQL query statement below
select request_at AS Day,
ROUND(sum(status!='completed')/COUNT(*),2) as 'Cancellation Rate'
FROM 
trips
LEFT JOIN users as clients on trips.client_id = clients.users_id
LEFT JOIN users as drivers on trips.driver_id = drivers.users_id
WHERE 
clients.banned = 'No'
AND drivers.banned='No'
AND request_at BETWEEN '2013-10-01'
AND '2013-10-03'
GROUP BY 
Day
# Write your MySQL query statement below
SELECT
I.invoice_id,
Cust.customer_name,
I.price,
COUNT(DISTINCT C.contact_name) as contacts_cnt,
COUNT(DISTINCT Nme.customer_name) AS trusted_contacts_cnt
FROM invoices I
LEFT JOIN Customers Cust on I.user_id = Cust.customer_id
LEFT JOIN Contacts C on C.user_id = Cust.customer_id
LEFT JOIN Customers Nme ON Nme.customer_name = C.contact_name
GROUP BY I.invoice_id
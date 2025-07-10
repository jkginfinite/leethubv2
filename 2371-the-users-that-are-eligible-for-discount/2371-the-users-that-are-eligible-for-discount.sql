CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
	# Write your MySQL query statement below.
	SELECT distinct user_id as user_id
    from purchases
    where time_stamp>=startDate and time_stamp<=endDate and amount>=minAmount
    order by user_id ASC;
END 
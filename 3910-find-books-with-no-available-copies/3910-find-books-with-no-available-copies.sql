# Write your MySQL query statement below
# Write your MySQL query statement below
with borrowed as
(select book_id, count(borrower_name) as current_borrowers
from borrowing_records
where return_date is NULL
group by 1)

select A.book_id, A.title, A.author, A.genre, A.publication_year, B.current_borrowers
from library_books A
join borrowed B
on A.book_id = B.book_id and A.total_copies = B.current_borrowers
order by current_borrowers DESC, title ASC
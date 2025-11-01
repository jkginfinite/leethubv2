with ranked as (
    SELECT
    student_id,
    subject,
    FIRST_VALUE(score) OVER (PARTITION BY student_id, subject ORDER BY exam_date) AS first_score,
    FIRST_VALUE(score) OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS latest_score
    FROM scores
)

SELECT DISTINCT *
FROM ranked
WHERE first_score<latest_score
ORDER BY student_id, subject
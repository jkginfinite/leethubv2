# Please, upvote if you like it. Thanks :-)
SELECT (CASE
            WHEN GREATEST(A, B, C) >= (A + B + C - GREATEST(A, B, C))
                THEN "Not A Triangle"
            WHEN (A=B AND B=C)
                THEN "Equilateral"
            WHEN (A=B OR B=C OR A=C)
                THEN "Isosceles"
            ELSE
                "Scalene"
        END) AS triangle_type
FROM Triangles
GROUP BY A, B, C
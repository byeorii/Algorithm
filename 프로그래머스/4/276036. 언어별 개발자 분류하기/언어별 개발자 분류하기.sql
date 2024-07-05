-- 코드를 작성해주세요
WITH frontend
     AS (SELECT Sum(code)
         FROM   skillcodes
         WHERE  category = "Front End"),
     grades
     AS (SELECT CASE
                  WHEN skill_code & (SELECT *
                                     FROM   frontend)
                       AND skill_code & (SELECT code
                                         FROM   skillcodes
                                         WHERE  NAME = "python") THEN 'A'
                  WHEN skill_code & (SELECT code
                                     FROM   skillcodes
                                     WHERE  NAME = "c#") THEN 'B'
                  WHEN skill_code & (SELECT *
                                     FROM   frontend) THEN 'C'
                END AS grade,
                id,
                email
         FROM   developers)
SELECT *
FROM   grades
WHERE  grade IS NOT NULL
ORDER  BY 1,
          2 
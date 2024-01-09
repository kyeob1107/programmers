-- 코드를 입력하세요
WITH RECURSIVE cte AS (
    SELECT 0 AS n
    UNION ALL
    SELECT n + 1 FROM cte WHERE n < 23
),
  hour_outs AS (
        SELECT hour(outs.DATETIME) HOUR,
            count(outs.ANIMAL_ID) COUNT
        FROM ANIMAL_OUTS outs
        GROUP BY hour(outs.DATETIME)
    )
    
SELECT cte.n,
        case when ho.COUNT is not null Then ho.COUNT
            when ho.COUNT is null THEN 0
        end COUNT
FROM cte
LEFT JOIN hour_outs ho on cte.n = ho.HOUR
ORDER BY cte.n
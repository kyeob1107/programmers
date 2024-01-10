-- 코드를 입력하세요
WITH join_2021 AS (
    SELECT count(USER_ID) cnt
    FROM USER_INFO info
    WHERE year(JOINED)='2021'
),
puchased_2021 AS (
    SELECT year(onl.SALES_DATE) YEAR, 
        month(onl.SALES_DATE) MONTH,
        count(distinct onl.USER_ID) PUCHASED_USERS
    FROM ONLINE_SALE onl
    JOIN USER_INFO info on onl.USER_ID = info.USER_ID
    WHERE year(JOINED)='2021'
    GROUP BY year(onl.SALES_DATE), month(onl.SALES_DATE)
)

SELECT p.YEAR, 
        p.MONTH,
        p.PUCHASED_USERS,
        round(p.PUCHASED_USERS/(SELECT j.cnt FROM join_2021 j),1) PUCHASED_RATIO
FROM puchased_2021 p
-- 코드를 입력하세요	
SELECT a.REST_ID , a.REST_NAME , a.FOOD_TYPE ,
            a.FAVORITES , a.ADDRESS , a.SCORE
FROM(
    SELECT info.REST_ID , info.REST_NAME , info.FOOD_TYPE ,
            info.FAVORITES ,info.ADDRESS,
            (SELECT round(avg(rev.REVIEW_SCORE),2)
                FROM REST_REVIEW rev GROUP BY rev.REST_ID
                HAVING rev.REST_ID = info.REST_ID) SCORE
    FROM REST_INFO info
    WHERE info.ADDRESS like '서울%'
    ORDER BY SCORE desc, info.FAVORITES desc)a
where a.SCORE is not null
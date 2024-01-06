-- 코드를 입력하세요
SELECT year(os.SALES_DATE) YEAR, month(os.SALES_DATE) MONTH,
        ui.GENDER GENDER , count(distinct os.user_id) USERS
FROM USER_INFO ui join ONLINE_SALE os on ui.USER_ID = os.USER_ID
WHERE ui.GENDER is not null
GROUP BY year(os.SALES_DATE),month(os.SALES_DATE),ui.GENDER
ORDER BY YEAR, MONTH, GENDER, USERS




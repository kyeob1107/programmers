-- 코드를 입력하세요
SELECT CATEGORY,PRICE Max_PRICE,PRODUCT_NAME
FROM FOOD_PRODUCT main
WHERE CATEGORY in ('과자','국','김치','식용유')
        and PRICE = (SELECT max(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY
                     HAVING CATEGORY = main.CATEGORY)
ORDER BY 2 desc
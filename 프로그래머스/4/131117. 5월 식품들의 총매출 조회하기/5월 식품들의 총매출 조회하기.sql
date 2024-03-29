-- 코드를 입력하세요
SELECT P.PRODUCT_ID, PRODUCT_NAME, SUM(PRICE*AMOUNT) TOTAL_SALES
FROM FOOD_PRODUCT P inner join FOOD_ORDER O on P.PRODUCT_ID=O.PRODUCT_ID
#WHERE date_format(PRODUCE_DATE,'%Y')=2022 and date_format(PRODUCE_DATE,'%m')=5
WHERE date_format(PRODUCE_DATE,'%Y-%m')='2022-05'
GROUP BY 1
ORDER BY 3 desc,1
-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, sum(TOTAL_ORDER) TOTAL_ORDER
FROM FIRST_HALF f inner join ICECREAM_INFO i on f.flavor = i.flavor
GROUP BY 1
ORDER BY 2
-- 코드를 입력하세요
SELECT distinct USER_ID, PRODUCT_ID
FROM ONLINE_SALE main
WHERE (SELECT PRODUCT_ID FROM ONLINE_SALE sub
        GROUP BY USER_ID,PRODUCT_ID
        HAVING COUNT(PRODUCT_ID)>1
                and sub.USER_ID=main.USER_ID and sub.PRODUCT_ID=main.PRODUCT_ID)
ORDER BY USER_ID, PRODUCT_ID desc
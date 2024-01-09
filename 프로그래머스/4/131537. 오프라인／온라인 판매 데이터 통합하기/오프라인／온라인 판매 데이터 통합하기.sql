-- 코드를 입력하세요
WITH MERGE_SALE as(
    SELECT date_format(onl.SALES_DATE,'%Y-%m-%d') SALES_DATE,
            onl.PRODUCT_ID, onl.USER_ID, onl.SALES_AMOUNT
    FROM ONLINE_SALE onl
    UNION
    SELECT date_format(offl.SALES_DATE,'%Y-%m-%d') SALES_DATE,
            offl.PRODUCT_ID, NULL USER_ID, offl.SALES_AMOUNT 
    FROM OFFLINE_SALE offl)

SELECT ms.SALES_DATE,ms.PRODUCT_ID,ms.USER_ID,ms.SALES_AMOUNT
FROM MERGE_SALE ms
WHERE year(ms.SALES_DATE)='2022' and month(ms.SALES_DATE)='03'
ORDER BY ms.SALES_DATE, ms.PRODUCT_ID,ms.USER_ID

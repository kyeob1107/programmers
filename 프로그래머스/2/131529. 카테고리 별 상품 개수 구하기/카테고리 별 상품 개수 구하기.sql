-- 코드를 입력하세요
SELECT  substr(PRODUCT_CODE,1,2) CATEGORY,
        count(1) PRODUCTS
from PRODUCT
group by 1
order by 1
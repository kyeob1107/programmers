-- 코드를 입력하세요
SELECT  substr(PRODUCT_CODE,1,2) CATEGORY,
        count(1) PRODUCTS
from PRODUCT
group by 1
order by 1

/*SELECT  PRODUCT_CODE,
        distinct(substr(PRODUCT_CODE,1,2)) CATEGORY#,
        #count(1) PRODUCTS
from PRODUCT
order by 1*/
#아래코드 안되는데 현재 왜 안되는지 모르겠어서 나중에 다시 확인
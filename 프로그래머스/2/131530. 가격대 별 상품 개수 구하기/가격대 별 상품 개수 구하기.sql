-- 코드를 입력하세요
SELECT case when price >=80000 then 80000
            when price >=70000 then 70000
            when price >=60000 then 60000
            when price >=50000 then 50000
            when price >=40000 then 40000
            when price >=30000 then 30000
            when price >=20000 then 20000
            when price >=10000 then 10000
            else 0 end PRICE_GROUP,
        count(price) PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY 1
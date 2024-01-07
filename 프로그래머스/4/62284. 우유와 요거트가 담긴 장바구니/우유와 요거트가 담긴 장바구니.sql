-- 코드를 입력하세요	 	
SELECT distinct pct.CART_ID
FROM CART_PRODUCTS pct
WHERE pct.CART_ID in (SELECT pct_mlik.CART_ID 
                        FROM CART_PRODUCTS pct_mlik
                        WHERE pct_mlik.NAME ='Milk' 
                        and pct_mlik.CART_ID=pct.CART_ID) 
    and pct.CART_ID in (SELECT pct_ygt.CART_ID 
                        FROM CART_PRODUCTS pct_ygt 
                        WHERE pct_ygt.NAME ='Yogurt' 
                        and pct_ygt.CART_ID = pct.CART_ID)
ORDER BY pct.CART_ID

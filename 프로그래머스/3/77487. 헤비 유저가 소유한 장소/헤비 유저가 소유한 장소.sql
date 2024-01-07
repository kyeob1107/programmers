-- 코드를 입력하세요
SELECT p.ID, p.NAME, p.HOST_ID
FROM PLACES p
WHERE p.HOST_ID = (SELECT p_sub.HOST_ID FROM PLACES p_sub 
                   GROUP BY p_sub.HOST_ID HAVING  count(p_sub.ID)>=2 
                        and p_sub.HOST_ID = p.HOST_ID)
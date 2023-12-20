-- 코드를 입력하세요
select DATETIME
from
(select NAME,DATETIME,
    rank() over(order by DATETIME) rn
from ANIMAL_INS)a
where rn = 1
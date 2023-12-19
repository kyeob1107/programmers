-- 코드를 입력하세요
select NAME
from
(select NAME,
    rank() over(order by DATETIME) rn
from ANIMAL_INS)a
where rn = 1

/*SELECT name
from ANIMAL_INS
order by DATETIME
limit 1*/

/*SELECT name
from ANIMAL_INS
where DATETIME=(select min(DATETIME) min_date
from ANIMAL_INS)*/





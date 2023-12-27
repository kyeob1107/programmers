-- 코드를 입력하세요
SELECT o.ANIMAL_ID,o.NAME #, (o.ANIMAL_ID-i.ANIMAL_ID) period
from ANIMAL_INS i left join ANIMAL_OUTS o on i.ANIMAL_ID=o.ANIMAL_ID
where o.ANIMAL_ID is not null
order by (o.DATETIME-i.DATETIME) desc
limit 2
-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.ANIMAL_TYPE, o.NAME
from ANIMAL_INS I inner join ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
where I.SEX_UPON_INTAKE like '%Intact%' and O.SEX_UPON_OUTCOME not like '%Intact%'
order by 1
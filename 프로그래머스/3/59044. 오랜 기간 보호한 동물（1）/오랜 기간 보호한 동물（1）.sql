-- 코드를 입력하세요
SELECT I.Name, I.datetime DATETIME
from ANIMAL_INS I left join ANIMAL_OUTS O on I.ANIMAL_ID=O.ANIMAL_ID
where O.Datetime is null
order by DATETIME #보호 시작일 순
limit 3 #가장 오래 있던 3마리
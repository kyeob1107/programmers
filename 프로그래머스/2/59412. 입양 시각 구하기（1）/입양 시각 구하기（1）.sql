-- 코드를 입력하세요
select HOUR,
        count(HOUR) COUNT
from
(SELECT datetime,time_format(time(datetime), '%H') HOUR
from ANIMAL_OUTS)a
where (HOUR>=9 and HOUR<20)
group by 1
order by 1
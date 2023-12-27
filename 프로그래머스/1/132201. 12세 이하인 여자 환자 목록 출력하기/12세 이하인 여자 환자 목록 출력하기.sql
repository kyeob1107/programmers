-- 코드를 입력하세요
SELECT PT_NAME,PT_NO,GEND_CD,AGE,
        if (TLNO is NUll,'NONE',TLNO) TLNO
from PATIENT
where (AGE <=12 and GEND_CD='W')
order by 4 desc,1
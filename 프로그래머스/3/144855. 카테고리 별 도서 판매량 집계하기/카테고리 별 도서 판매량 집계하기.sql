-- 코드를 입력하세요
SELECT CATEGORY,
        sum(SALES) TOTAL_SALES
from BOOK B inner join BOOK_SALES BS on B.BOOK_ID = BS.BOOK_ID
where year(SALES_DATE)=2022 and month(SALES_DATE)=1
group by 1
order by 1
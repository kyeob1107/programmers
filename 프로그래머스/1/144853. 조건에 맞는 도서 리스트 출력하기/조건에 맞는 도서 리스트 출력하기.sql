-- 코드를 입력하세요
SELECT BOOK_ID,
    date_format(PUBLISHED_DATE,'%Y-%m-%d') PUBLISHED_DATE
FROM BOOK
WHERE date_format(PUBLISHED_DATE,'%Y-%m-%d')=2021 and CATEGORY = '인문'
#ORDER BY 2
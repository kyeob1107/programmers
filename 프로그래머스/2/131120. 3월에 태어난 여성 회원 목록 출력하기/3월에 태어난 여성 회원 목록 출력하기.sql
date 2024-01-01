-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH,'%Y-%m-%d')
FROM MEMBER_PROFILE
WHERE date_format(DATE_OF_BIRTH,'%m-%d')=3 and GENDER = 'W' and TLNO is not null
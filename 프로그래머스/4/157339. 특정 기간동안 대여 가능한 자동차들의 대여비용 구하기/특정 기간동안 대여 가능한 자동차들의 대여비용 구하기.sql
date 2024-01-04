-- 코드를 입력하세요
WITH CANDIATE_LIST as(
    SELECT rental.CAR_ID, rental.CAR_TYPE,
        round(30*rental.DAILY_FEE *(1-(SELECT disc.DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN disc where disc.DURATION_TYPE = '30일 이상' and disc.CAR_TYPE = rental.CAR_TYPE)/100)) FEE
FROM CAR_RENTAL_COMPANY_CAR rental
    join CAR_RENTAL_COMPANY_RENTAL_HISTORY history
    on rental.CAR_ID = history.CAR_ID
WHERE rental.CAR_TYPE in ('세단','SUV') 
GROUP BY rental.CAR_ID
HAVING max(END_DATE)<'2022-11-01'
)
SELECT distinct c_list.CAR_ID, c_list.CAR_TYPE, c_list.FEE
FROM CANDIATE_LIST c_list
WHERE c_list.FEE BETWEEN 500000 and 1999999
ORDER BY c_list.FEE desc, c_list.CAR_TYPE, c_list.CAR_ID desc
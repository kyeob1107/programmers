-- 코드를 입력하세요
SELECT month(hst.START_DATE) MONTH,hst.CAR_ID,
        count(hst.START_DATE) RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY hst
WHERE 
    hst.CAR_ID=(SELECT hst_sub.CAR_ID
                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY hst_sub
                WHERE date_format(hst_sub.START_DATE,'%Y-%m') 
                        between '2022-08' and '2022-10'
                GROUP BY hst_sub.CAR_ID
                HAVING count(hst_sub.START_DATE)>=5
                        and hst_sub.CAR_ID=hst.CAR_ID)
    and date_format(hst.START_DATE,'%Y-%m') 
            between '2022-08' and '2022-10'
GROUP BY month(hst.START_DATE),hst.CAR_ID
ORDER BY MONTH, CAR_ID desc
-- 코드를 입력하세요
SELECT hst.HISTORY_ID, hst.CAR_ID,
        date_format(hst.START_DATE,'%Y-%m-%d') START_DATE,
        date_format(hst.END_DATE,'%Y-%m-%d') END_DATE,
        case 
            when datediff(hst.END_DATE,hst.START_DATE)+1>=30 then "장기 대여"
            else "단기 대여"
        end RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY hst
WHERE date_format(hst.START_DATE,'%Y-%m') ='2022-09'
ORDER BY hst.HISTORY_ID desc
#WHERE date_format(hst.START_DATE,'%Y-%m-%d') BETWEEN '2022-09-01' and '2022-09-31'



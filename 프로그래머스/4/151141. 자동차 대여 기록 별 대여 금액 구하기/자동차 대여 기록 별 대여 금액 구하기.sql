-- 코드를 입력하세요
With truck_discount AS(

    SELECT disc.CAR_TYPE,
            substr(disc.DURATION_TYPE,1,locate('일',disc.DURATION_TYPE)-1) duration_type,
            disc.DISCOUNT_RATE
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN disc
    WHERE disc.CAR_TYPE = '트럭'

),

truck_table AS(

SELECT hst.HISTORY_ID, car.CAR_TYPE, 
    car.DAILY_FEE * (datediff(hst.END_DATE,hst.START_DATE)+1) pre_fee,
    case 
        when datediff(hst.END_DATE,hst.START_DATE)+1>=90
        then 90
        when datediff(hst.END_DATE,hst.START_DATE)+1 between 30 and 89
        then 30
        when datediff(hst.END_DATE,hst.START_DATE)+1 between 7 and 29
        then 7
        else 0
    end duration_type
FROM CAR_RENTAL_COMPANY_CAR car
join CAR_RENTAL_COMPANY_RENTAL_HISTORY hst on car.CAR_ID = hst.CAR_ID
WHERE car.CAR_TYPE = '트럭'

)

SELECT distinct tt.HISTORY_ID,
        case when tt.duration_type=0 then tt.pre_fee
            else ROUND(tt.pre_fee * (1-(td.DISCOUNT_RATE/100)))
            end FEE
FROM truck_table tt
JOIN truck_discount td on tt.CAR_TYPE=td.CAR_TYPE
WHERE tt.DURATION_TYPE = td.DURATION_TYPE or tt.DURATION_TYPE = 0
ORDER BY FEE desc, tt.HISTORY_ID desc

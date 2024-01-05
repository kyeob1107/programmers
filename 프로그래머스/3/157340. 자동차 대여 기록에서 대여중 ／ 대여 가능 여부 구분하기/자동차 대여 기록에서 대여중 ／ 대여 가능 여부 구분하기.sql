-- 코드를 입력하세요
SELECT hist.CAR_ID,
    case
        when max(hist.end_date)<'2022-10-16' then "대여 가능"
        else "대여중"
    end AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY hist
where hist.start_date<='2022-10-16'
GROUP BY hist.CAR_ID
order by 1 desc
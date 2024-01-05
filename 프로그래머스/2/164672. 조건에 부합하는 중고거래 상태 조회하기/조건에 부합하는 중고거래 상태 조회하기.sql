-- 코드를 입력하세요
SELECT board.BOARD_ID, board.WRITER_ID , board.TITLE , board.PRICE,
        case
            when board.STATUS='SALE' then "판매중"
            when board.STATUS='RESERVED' then "예약중"
            when board.STATUS='DONE' then "거래완료"
        end STATUS
FROM USED_GOODS_BOARD board
WHERE CREATED_DATE='2022-10-05'
ORDER BY board.BOARD_ID desc
-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME,
    concat(u.CITY,' ',u.STREET_ADDRESS1,' ',u.STREET_ADDRESS2) "전체주소",
    concat(substr(TLNO,1,3),'-',substr(TLNO,4,4),'-',substr(TLNO,8,4)) "전화번호" #, count(b.board_id) count_board
FROM USED_GOODS_BOARD b right join USED_GOODS_USER u on b.WRITER_ID = u.USER_ID
#USER라고 적으니 따로  함수가 있는듯하여 짧게 u만 사용(하는김에 b도 짧게)
GROUP BY u.USER_ID
HAVING count(b.BOARD_ID)>=3
ORDER BY u.USER_ID desc
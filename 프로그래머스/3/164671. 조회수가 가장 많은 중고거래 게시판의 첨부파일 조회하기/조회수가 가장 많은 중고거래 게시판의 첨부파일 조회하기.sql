-- 코드를 입력하세요
SELECT concat('/home/grep/src/',brd.BOARD_ID,'/',file.FILE_ID,file.FILE_NAME,file.FILE_EXT) FILE_PATH
FROM USED_GOODS_FILE file join USED_GOODS_BOARD brd on file.BOARD_ID = brd.BOARD_ID
WHERE brd.VIEWS = (select max(brd_sub.VIEWS) from USED_GOODS_BOARD brd_sub where brd_sub.VIEWS=VIEWS)
ORDER BY file.FILE_ID desc
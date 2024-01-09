-- 코드를 입력하세요
WITH REVIW_MERGE as(
        SELECT pro.MEMBER_NAME,
               rev.MEMBER_ID,
               rev.REVIEW_TEXT, 
               date_format(rev.REVIEW_DATE,'%Y-%m-%d') REVIEW_DATE
        FROM REST_REVIEW rev 
        JOIN MEMBER_PROFILE pro on rev.MEMBER_ID=pro.MEMBER_ID
    
    ), 
    Count_review as(
            SELECT rev_sub.MEMBER_ID, 
            count(rev_sub.REVIEW_ID) cnt_review
            FROM REST_REVIEW rev_sub
            GROUP BY rev_sub.MEMBER_ID
            )
SELECT rm.MEMBER_NAME,
       rm.REVIEW_TEXT,
       rm.REVIEW_DATE
FROM REVIW_MERGE rm
JOIN Count_review cnt on rm.MEMBER_ID = cnt.MEMBER_ID
WHERE cnt.cnt_review = (SELECT MAX(cnt_review) FROM Count_review)
ORDER BY rm.REVIEW_DATE, rm.REVIEW_TEXT
       

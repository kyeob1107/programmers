-- 코드를 입력하세요
SELECT appo.APNT_NO,
        (SELECT pt.PT_NAME FROM PATIENT pt WHERE pt.PT_NO = appo.PT_NO) PT_NAME,
        appo.PT_NO, appo.MCDP_CD,
        (SELECT dr.DR_NAME FROM DOCTOR dr WHERE dr.DR_ID=appo.MDDR_ID) DR_NAME,
        appo.APNT_YMD
FROM APPOINTMENT appo
WHERE date_format(appo.APNT_YMD,'%Y-%m-%d') = '2022-04-13'
			and appo.APNT_CNCL_YN = 'N' and appo.MCDP_CD='CS'
ORDER BY appo.APNT_YMD
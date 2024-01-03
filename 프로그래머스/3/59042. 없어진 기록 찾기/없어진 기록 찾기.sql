-- 코드를 입력하세요
SELECT outs.animal_id, outs.name
FROM ANIMAL_INS ins right join ANIMAL_OUTS outs on ins.animal_id = outs.animal_id
WHERE outs.animal_id is not null and ins.animal_id is null
-- 코드를 입력하세요
SELECT ANIMAL_TYPE,
        count(1) count
from ANIMAL_INS
#where ANIMAL_TYPE like '%Cat%' or ANIMAL_TYPE like '%Dog%'
#혹시 데이터에 개,고양이말고도 있을까 넣어뒀지만 빼고해도 둘만 있는 것을 확인하여
#주석처리
group by 1
order by 1
#알파벳순이 아니라 만약 특정 원하는 순서가 있을시 그 정해준 순서로도 가능한지?
#만약 개, 고양이, 사자, 얼룩말 이라고 하면 순서대로면 개,고양이,사자,얼룩말인데
#사자,고양이,개,얼룩말 이런식으로 임의의 순서로 정하는게 가능한지
# pypy 1등 코드를 python으로 제출하면 어떤지 궁금, 비교
from itertools import combinations
n,k = map(int,input().split())
if k < 5:
    print(0)

else:
    k -= 5
    word=[]
    study ={'a','n','t','i','c'}
    alpha = {key: v for v, key in enumerate((set(map(chr,range(ord('a'), ord('z')+1))) - study))}
    cnt = 0
    for _ in range(n):
        temp = 0
        for i in set(input())-study:
            temp |= (1<<alpha[i])
        word.append(temp)
    count = (2**j for j in range(21))
    for comb in combinations(count,k):
        test = sum(comb)
        ct = 0
        for cb in word:
            if test&cb == cb:
                ct +=1
        cnt = max(cnt,ct)
    print(cnt)
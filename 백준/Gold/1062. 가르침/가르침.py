# 레퍼런스 참고해서 작성
import sys
from itertools import combinations

input = sys.stdin.readline
N, K = map(int, input().split())
if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    essential = {'a', 'n', 't', 'i', 'c'}
    words = [input()[4:-4] for _ in range(N)]
    all_need = set()
    for word in words:
        all_need = all_need | set(word)
    all_need -= essential
    
    if len(all_need) + 5 <= K:
        print(N)
    
    else:
        res = 0
        for comb in combinations(all_need, K-5):
            learn = set(comb) | essential
            cnt = N
            for word in words:
                for w in word:
                    if w not in learn:
                        cnt -= 1
                        break
            if cnt > res:
                res = cnt
        print(res)
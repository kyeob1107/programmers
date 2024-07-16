# 레퍼런스 원본
from itertools import combinations

def solve():
    N, K  = map(int, input().split())
    if K < 5:
        return 0
    if K == 26:
        return N

    essential = {'a', 'n', 't', 'i', 'c'}
    words = [input()[4:-4] for _ in range(N)]

    all_need = set()
    for i in range(N):
        for char in words[i]:
            if char not in essential:
                all_need.add(char)

    if len(all_need) + 5 <= K:
        return N

    MAX = 0
    for comb in combinations(all_need, K-5):
        comb = set(comb) | essential
        cnt = 0
        for word in words:
            for char in word:
                if char not in comb:         # 변경부분
                    break                    # 변경부분
            else:                            # 변경부분
                cnt += 1                     # 변경부분
        if cnt > MAX:
            MAX = cnt
    return MAX
print(solve())
# 2차시도 정렬 먼저하고 글자순대로 배치
import sys
input = sys.stdin.readline
N = int(input())
word_len = [0] * 50
data = []
for _ in range(N):
    w_temp = input().strip()
    if w_temp not in data:
        data.append(w_temp)
    if not word_len[len(w_temp) - 1]:
        word_len[len(w_temp) - 1] = 1
lens = [l + 1 for l, c in enumerate(word_len) if c]
data.sort()
ans = []
for l in lens:
    ans += [s for s in data if len(s) == l]
for p in ans:
    print(p)
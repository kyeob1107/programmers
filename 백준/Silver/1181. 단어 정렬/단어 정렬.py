import sys
input = sys.stdin.readline
N = int(input())
data = dict()
ans = []
for _ in range(N):
    word = input().strip()
    if len(word) in data:
        data[len(word)].append(word)
    else:
        data[len(word)] = [word]

for l in sorted(data.keys()):
    data[l].sort()
    for s in data[l]:
        if s not in ans:
            ans.append(s)
        
for p in ans:
    print(p)
# 2등 코드 이해용
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
i,*q = range(n+1)

result = []
for p in q[::-1]:
    i = ( i + k - 1) % p
    result.append(q.pop(i))

ans = str(result)[1:-1]
print(f"<{ans}>")
import sys

def cnt_entry_exit(x1, y1, x2, y2, n):
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        
        if ((x1 - cx)**2 + (y1 -cy)**2 - r**2) * ((x2 - cx)**2 + (y2 -cy)**2 - r**2) < 0:
            cnt += 1
        
    return cnt

input = sys.stdin.readline
T = int(input())
results = []
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    results.append(cnt_entry_exit(x1, y1, x2, y2, N))

for result in results:
    print(result)
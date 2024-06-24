import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pos = list(map(int, input().split()))
for i in range(M):
    for j in range(i + 1, M):
        if pos[j] > pos[i]:
            pos[j] -=1
head = 1
ans = 0
for p in pos:
    while True:
        if head == p:
            N-=1
            break
        else:
            move = min((p - head) % N, (N - (p - head) % N))
            head = p
            ans += move
        
print(ans)
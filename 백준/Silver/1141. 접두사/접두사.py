import sys
input = sys.stdin.readline

N = int(input())
word_list = []
for _ in range(N):
    word_list.append(input().strip())

word_list.sort(key=len)
cnt = 0

for i in range(N):
    prefix = False
    if all(not word_list[j].startswith(word_list[i]) for j in range(i + 1, N)):
        cnt += 1
print(cnt)
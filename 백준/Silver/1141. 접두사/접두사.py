# 1등 코드 확인용
import sys
input = sys.stdin.readline


n = int(input())
string_set = [input().strip() for _ in range(n)]
string_set.sort()
answer = 1
for i in range(1, n):
    if string_set[i-1] != string_set[i][:len(string_set[i-1])]:
        answer += 1

print(answer)
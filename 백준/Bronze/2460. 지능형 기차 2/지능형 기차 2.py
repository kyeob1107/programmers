import sys
input = sys.stdin.readline

num = 0
max_num = 0
for _ in range(10):
    down, up = map(int, input().split())
    num = num - down + up
    if max_num < num:
        max_num = num

print(max_num)
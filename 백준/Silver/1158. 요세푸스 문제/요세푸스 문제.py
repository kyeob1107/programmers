import sys
input = sys.stdin.readline

N, K = map(int, input().split())
result = []
remain_list = [*range(1, N+1)]

pop_index = 0
while remain_list:
    pop_index = (pop_index + K - 1) % len(remain_list)
    result.append(remain_list.pop(pop_index))

ans = ", ".join(map(str,result))
print(f"<{ans}>")
# 다른 분 것 참고
import sys
input = sys.stdin.readline

def dfs(idx, result, add, sub, mul, div):
    global max_res, min_res
    if idx == N:
        max_res = max(max_res, result)
        min_res = min(min_res, result)
        return 
    if add > 0:
        dfs(idx + 1, result + series[idx], add - 1, sub, mul, div)
    if sub > 0:
        dfs(idx + 1, result - series[idx], add, sub - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, result * series[idx], add, sub, mul - 1, div)
    if div > 0:
        dfs(idx + 1, int(result / series[idx]), add, sub, mul, div - 1)

N = int(input())
series = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # + - * //
min_res = 10**9
max_res = -10**9
dfs(1, series[0], add, sub, mul, div)
print(max_res)
print(min_res)
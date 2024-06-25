import sys
input = sys.stdin.readline

def square(N, M):
    for r  in range(min(N, M), 0, -1):
        for i in range(N - r):
            for j in range(M - r):
                if rectangle[i][j] == rectangle[i][j + r] == rectangle[i + r][j] == rectangle[i + r][j + r]:
                    return (r + 1) ** 2
    return 1

N, M = map(int, input().split())
rectangle = [[int(n) for n in input().strip()] for _ in range(N)]
print(square(N, M))
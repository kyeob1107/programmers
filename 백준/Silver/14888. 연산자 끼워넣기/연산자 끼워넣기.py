# pypy3 1등 코드 살짝 이해 편하게 수정해서 테스트해보는 용
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))

P = {(0, 0, 0, 0): [A[0], A[0]]}
for i in range(1, n):
    P_ = {}
    f = (
        lambda k, z: k + z,
        lambda k, z: k - z,
        lambda k, z: k * z,
        lambda k, z: k // z if k > 0 else -(-k // z)
    )
    for x in P:
        for j in range(4):
            if x[j] < O[j]:
                _ = list(x)
                _[j] += 1
                _ = tuple(_)
                u = f[j](P[x][0], A[i])
                v = f[j](P[x][1], A[i])
                if u < v:
                    u, v = v, u
                if _ in P_:
                    P_[_] = [max(P_[_][0], u), min(P_[_][1], v)]
                else:
                    P_[_] = [u, v]
    P = P_
for i in P[tuple(O)]:
    print(i)
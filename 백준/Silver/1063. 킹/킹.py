# 1등 코드 확인용
import sys
input = sys.stdin.readline
c = {chr(i+64):i for i in range(1,9)}
c_r = {i:chr(i+64) for i in range(1,9)}
dir = {"R": (0,1),"L": (0,-1),"B": (-1,0),"T": (1,0),
       "RT": (1,1),"LT": (1,-1),"RB": (-1,1),"LB": (-1,-1)}

k,s,n = input().split()
kx, ky = int(k[1]),c[k[0]]
sx, sy = int(s[1]),c[s[0]]
for _ in range(int(n)):
    i,j = dir[input().strip()]
    nkx, nky = kx + i, ky + j
    if nkx == sx and nky == sy:
        nsx, nsy = sx + i, sy + j
        if 0 < nsx <= 8 and 0 < nsy <= 8:
            kx, ky, sx, sy = nkx, nky, nsx, nsy
    elif 0 < nkx <= 8 and 0 < nky <= 8:
        kx, ky = nkx, nky
print("".join(map(str,[c_r[ky],kx])))
print("".join(map(str,[c_r[sy],sx])))
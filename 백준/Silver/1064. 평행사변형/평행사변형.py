import sys
input = sys.stdin.readline

xa, ya, xb, yb, xc, yc = map(int, input().split())
r1 = ((xa - xb)**2 + (ya - yb)**2)**0.5
r2 = ((xc - xb)**2 + (yc - yb)**2)**0.5
r3 = ((xc - xa)**2 + (yc - ya)**2)**0.5
r = [r1, r2, r3]

if ((xa-xb)*(ya-yc)==(ya-yb)*(xa-xc)):
    print(-1.0)
else:
    print((max(r) - min(r)) * 2)
import sys

def d(x1, y1, x2, y2):
    result = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if result%1 == 0:
        result = int(result)
    return result
input = sys.stdin.readline
# input = open("input.txt", "rt").readline
T = int(input())
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # print(x1, y1, r1, x2, y2, r2)
    if (x1, y1) == (x2, y2):
        if r1 == r2:
            print(-1)
        else:
            print(0)
    
    else:
        distance = d(x1, y1, x2, y2)
        if distance < r1 + r2 and distance > abs(r1 - r2) :
            print(2)
        elif distance == r1 + r2 or distance == abs(r1 - r2):
            print(1)
        else:
            print(0)
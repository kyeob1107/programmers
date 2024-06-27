import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = (Y * 100) // X

if Z > 98:
    print(-1)

else:
    start = 0
    end = X
    
    while start <= end:
        mid = (start + end)//2
        if (Y+mid)*100//(X+mid) > Z:
            end = mid - 1
        else:
            start = mid + 1
            
    print(start)
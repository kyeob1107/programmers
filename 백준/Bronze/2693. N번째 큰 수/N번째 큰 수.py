# 내장 함수 최대한 안쓰고 해보기 # 모아뒀다가 프린트 따로
import sys

def n_largest(array):
    largest = []
    for i in array:
        if len(largest) < 3:
            if not largest:
                largest.append(i)
            else:
                if i >= largest[0]:
                    largest.insert(0, i)
                elif i < largest[-1]:
                    largest.append(i)
                else:
                    largest.insert(1, i)
                    
        else:
            if i >= largest[0]:
                largest.insert(0, i)
            elif i >= largest[1]:
                largest.insert(1, i)
            elif i >= largest[2]:
                largest.insert(2, i)
            
            if len(largest) > 3:
                largest.pop()
    return largest[-1]

input = sys.stdin.readline
T = int(input())
ans = []
for _ in range(T):
    ans.append(n_largest(list(map(int, input().split()))))

for p in ans:
    print(p)
# 뤼튼한테 개선해보라 해서 얻은 코드
import sys
input = sys.stdin.readline

N = int(input())

def is_hansu(num):
    str_num = str(num)
    if len(str_num) <= 2:
        return True
    diff = int(str_num[1]) - int(str_num[0])
    for i in range(1, len(str_num) - 1):
        if int(str_num[i + 1]) - int(str_num[i]) != diff:
            return False
    return True

if N < 100:
    print(N)
else:
    cnt = 99
    for i in range(100, N + 1):
        if is_hansu(i):
            cnt += 1
    print(cnt)

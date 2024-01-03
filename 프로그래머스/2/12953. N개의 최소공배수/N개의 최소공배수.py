def LCM(a, b): #유클리드 호제법으로 잘짜둔것 가져온것
    c,d = max(a, b), min(a, b)
    t = 1
    while t>0:
        t = c%d
        c, d = d, t
    return int (a*b/c)

def solution(arr):
    lcm_num=1
    for i in range(len(arr)):
        lcm_num=LCM(lcm_num,arr[i])
    return lcm_num
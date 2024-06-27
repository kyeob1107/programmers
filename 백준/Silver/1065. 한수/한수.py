import sys
input = sys.stdin.readline

N =  int(input())
N_len = len(str(N))

if N_len <=2:
    print(N)
elif 999 <= N <= 1000:
    print(144)
else:
    first_num = N//10**(N_len - 1)
    r_list = [i for i in range((9 - first_num) // (N_len - 1), -1, -1)] + [i for i in range(-1, -1 * (first_num // (N_len - 1)) - 1, -1)]
    ans = 99 + (first_num) * len(r_list)
    for i, r in enumerate(r_list):
        temp = [(first_num + r*m) * 10**((N_len-1) - m) for m in range(N_len)]
        number = sum(temp)
        if number <= N:
            ans -= i
            break
    if number > N:
        ans -= len(r_list)
    print(ans)
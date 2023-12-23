def solution(n):
    #3진법으로 변환 과정(뒤집힌 순으로 되어있음)
    rev_base = []
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base.append(mod)
    print(rev_base)

    answer=0
    for i in range(len(rev_base)):
        answer+=(3**i)*rev_base[::-1][i]
    return answer
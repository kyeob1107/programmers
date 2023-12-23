def divisor(num):
    lt = []
    
    for i in range(num):
        if num % (i + 1) == 0:
            lt.append(i + 1)
            
    return lt

def solution(n, m):
    lt_n = divisor(n)
    lt_m = divisor(m)
    gcd = 1
    
    for i in lt_n:
        for j in lt_m:
            if i == j and i > gcd:
                gcd = i
                
    lcm = n * m / gcd
    
    return [gcd, lcm]
import sys
input = sys.stdin.readline

def Z(N, r, c):
    if r == 0 and c == 0:
        return 0
    
    elif r == 0 and c == 1:
        return 1
    
    elif r == 1 and c == 0:
        return 2
    
    elif r == 1 and c == 1:
        return 3
    
    else:
        num_i = 2 ** (N - 1)
        val = num_i ** 2
        if r < num_i and c < num_i:
            return Z(N - 1, r, c)
        
        elif r < num_i and c >= num_i:
            return val + Z(N - 1, r, c - num_i)
        
        elif r >= num_i and c < num_i:
            return 2 * val + Z(N - 1, r - num_i, c)
        
        elif r >= num_i and c >= num_i:
            return 3 * val + Z(N - 1, r - num_i, c - num_i)

N, r, c = map(int, input().split())
print(Z(N, r, c))
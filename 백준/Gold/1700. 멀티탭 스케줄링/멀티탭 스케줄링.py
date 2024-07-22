import sys
input = sys.stdin.readline
N, K = map(int, input().split())
use_history = list(map(int, input().split())) 
use_order = {}
for i, u in enumerate(use_history):
    if u in use_order:
        use_order[u].append(i)
    else:
        use_order[u] = [i]

if len(use_order.keys()) <= N:
    print(0)
else:
    use_history.reverse()
    res = 0
    multitab = [] #[0] * N
    
    for i in range(K):
        use = use_history.pop()
        use_order[use].remove(i)
        if use not in multitab:
            if len(multitab) < N:
                multitab.append(use)
            else:
                next_order = [[u, use_order[u][0]] if len(use_order[u]) > 0 else [u, K+1] for u in multitab]
                later_use = max(next_order, key=lambda x: x[1])[0]
                multitab.remove(later_use)
                multitab.append(use)
                res += 1
    print(res)
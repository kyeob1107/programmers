# 뤼튼에게 개선해달라고 하면서 알게된 것 sorted의 key인자를 활용하면 한번에 여러기준으로 정렬 바로 가능함
import sys
input = sys.stdin.readline

N = int(input().strip())
data = set()

for _ in range(N):
    w_temp = input().strip()
    data.add(w_temp)

# 데이터를 길이와 사전순으로 정렬
sorted_data = sorted(data, key=lambda x: (len(x), x))

for word in sorted_data:
    print(word)
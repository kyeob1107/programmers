import sys
input = sys.stdin.readline

N = int(input())
before = dict()
sequence = [0]*N

for i, num in enumerate(map(int, input().split())):
    if num not in before:
        before[num] = [i]
    else:
        before[num].append(i)

value = 0
for num in sorted(before):
    for index in before[num]:
        sequence[index] = value
        value += 1
print(*sequence)
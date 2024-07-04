# 6등 코드 5등 코드와 비슷 확인용
import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for i in range(n)]
words = list(set(words))
words.sort()
words.sort(key=len)

print('\n'.join(words))
import sys
input = sys.stdin.readline
print(bin(int(input()))[2:].count('1'))
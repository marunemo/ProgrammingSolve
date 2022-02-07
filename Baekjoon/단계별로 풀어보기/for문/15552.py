# fast IO
from sys import stdin
input = stdin.readline

t = int(input())
totalList = []
for _ in range(t):
    a, b = map(int, input().split())
    totalList.append(a + b)

print(*totalList, sep="\n")
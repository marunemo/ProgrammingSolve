# fast IO
from sys import stdin
input = stdin.readline

t = int(input())
totalList = []
for _ in range(t):
    a, b = map(int, input().split())
    totalList.append(a + b)

for i, c in enumerate(totalList):
    print("Case #{0}: {1}".format(i + 1, c))
# fast IO
from sys import stdin
input = stdin.readline

t = int(input())
totalList = []
for _ in range(t):
    a, b = map(int, input().split())
    totalList.append([a, b, a + b])

for i, total in enumerate(totalList):
    print("Case #%d: %d + %d = %d" % (i + 1, *total))
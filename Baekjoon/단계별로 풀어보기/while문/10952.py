from sys import stdin

totalList = []
while True:
    a, b = map(int, stdin.readline().split())
    if a == 0 and b == 0:
        break
    totalList.append(a + b)
print(*totalList, sep="\n")
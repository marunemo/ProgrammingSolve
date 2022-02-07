from sys import stdin

totalList = []
try:
    while True:
        a, b = map(int, stdin.readline().split())
        totalList.append(a + b)
except:
    print(*totalList, sep="\n")
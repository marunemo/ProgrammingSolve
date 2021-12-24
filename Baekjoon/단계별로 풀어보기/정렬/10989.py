from sys import stdin

cases = int(input())
num = dict()

for _ in range(cases):
    n = int(stdin.readline())
    try:
        num[n] += 1
    except KeyError:
        num[n] = 1

for n,count in sorted(num.items()):
    for _ in range(count):
        print(n)
# fast IO
from sys import stdin
readIntegers = lambda : map(int, stdin.readline().split())

n, x = readIntegers()
a = readIntegers()

for i in a:
    if i < x:
        print(i, end=" ")
from sys import setrecursionlimit
setrecursionlimit(100001)

def gotoN(n, step = 1):
    print(step)
    if step != n:
        gotoN(n, step + 1)

n = int(input())
gotoN(n)
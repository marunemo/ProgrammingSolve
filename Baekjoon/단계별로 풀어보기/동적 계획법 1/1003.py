def fibo(n):
    n1 = [1, 0]
    n2 = [0, 1]
    for _ in range(n):
        n1, n2 = n2, [n1[0] + n2[0], n1[1] + n2[1]]
    return n1

t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))

for i in n:
    print(*fibo(i))
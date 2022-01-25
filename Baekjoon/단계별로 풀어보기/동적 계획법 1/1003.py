def fibo(n):
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        n1 = fibo(n - 1)
        n2 = fibo(n - 2)
        return [n1[0] + n2[0], n1[1] + n2[1]]   

t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))

for i in n:
    print(*fibo(i))
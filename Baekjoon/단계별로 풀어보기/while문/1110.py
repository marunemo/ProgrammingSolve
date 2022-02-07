n = int(input())
a, b = n // 10, n % 10
na, nb = a, b

a, b = b, (a + b) % 10
count = 1
while a != na or b != nb:
    a, b = b, (a + b) % 10
    count += 1
print(count)
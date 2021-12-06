a = int(input())
b = int(input())

add = 0
exponent = 1
while b > 0:
    digitAdd = a * (b % 10)
    print(digitAdd)
    add += digitAdd * exponent
    b = b // 10
    exponent *= 10
print(add)
from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def awesomePrime(num, digit, n):
    if digit == n:
        print(num)
        return

    num *= 10
    for i in [1, 3, 7, 9]:
        if isPrime(num + i):
            awesomePrime(num + i, digit + 1, n)

prime = [2, 3, 5, 7]

n = int(input())

digit = 1
for num in prime:
    awesomePrime(num, digit, n)
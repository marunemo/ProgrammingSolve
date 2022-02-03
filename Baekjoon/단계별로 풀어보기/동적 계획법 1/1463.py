def calcX(x):
    if x == 1:
        return 0

    count = []
    if x % 3 == 0:
        count.append(calcX(x // 3) + 1)
    if x % 2 == 0:
        count.append(calcX(x // 2) + 1)
    count.append(calcX(x - 1) + 1)
    return min(count)

n = int(input())
print(calcX(n))
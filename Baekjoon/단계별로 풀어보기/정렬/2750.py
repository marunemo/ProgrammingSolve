cases = int(input())
num = []

for _ in range(cases):
    num.append(int(input()))

print(*sorted(num), sep="\n")
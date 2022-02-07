t = int(input())

case = []
for _ in range(t):
    a, b = map(int, input().split())
    case.append(a + b)

print(*case, sep="\n")
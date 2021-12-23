cases = int(input())
num = []

for _ in range(cases):
    num.append(int(input()))

num.sort()
for i in num:
    print(i)
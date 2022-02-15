'''
풀이

전깃줄이 교차하는 경우는 하나 이상의 줄에 대하여 다른 전깃줄이 그 증감을 따라가지 못하면 발생한다.
다시 말해, f:A -> B인 전깃줄이라고 할 때,
x < y에 대하여 f(x) > f(y)인 경우가 발생하면 전깃줄이 교차하게 된다.
'''

# fast IO
from sys import stdin

# 줄의 개수와 전봇대에 연결된 줄 입력
lineCount = int(stdin.readline())
lines = []
for _ in range(lineCount):
    line = list(map(int, stdin.readline().split()))
    lines.append(line)

# 전깃줄을 A 전봇대에 대하여 정렬
lines.sort()

# B 전봇대에 대하여 LIS의 길이 탐색
maxB = 0
increaseB = 0
for _, b in lines:
    if maxB < b:
        maxB = b
        increaseB += 1

# 전깃줄을 B 전봇대에 대하여 정렬
lines.sort(key=lambda x: (x[1], x[0]))

# A 전봇대에 대하여 LIS의 길이 탐색
maxA = 0
increaseA = 0
for a, _ in lines:
    if maxA < a:
        maxA = a
        increaseA += 1

# x < y에 대하여 f(x) > f(y)을 따르지 않는 전깃줄 개수 출력
print(lineCount - max(increaseA, increaseB))
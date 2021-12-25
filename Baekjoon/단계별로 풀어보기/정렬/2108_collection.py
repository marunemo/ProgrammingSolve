from collections import Counter
from sys import stdin

# 구해야 하는 값
average = 0
median = 0
mode = 0
width = 0

# 입력 값
cases = int(input())
score = []
for _ in range(cases):
    i = int(stdin.readline())
    score.append(i)
    average += i
score.sort()

# 평균 (소수점 첫째 자리에서 반올림)
average = int(round(average / cases, 0))

# 중앙값 (중앙 인덱스)
median = score[cases // 2]

# 최빈값
count = Counter(score).most_common()
if cases == 1:
    mode = count[0][0]
elif count[0][1] == count[1][1]:
    mode = count[1][0]
else:
    mode = count[0][0]

# 범위 (최댓값 - 최솟값)
width = score[-1] - score[0]

# 결과 출력
print(average)
print(median)
print(mode)
print(width)
from sys import stdin

# 구해야 하는 값
average = 0
median = 0
mode = 0
width = 0

# 입력 저장
score = dict()
cases = int(input())

# cases개만큼 점수 입력
for _ in range(cases):
    i = int(stdin.readline())
    average += i
    try:
        score[i] += 1
    except KeyError:
        score[i] = 1

# 산술 평균 (소수점 첫째에서 반올림)
average = int(round(average / cases, 0))

# 중앙값 (현재 점수까지의 인덱스 총 개수의 절반 이상인지 확인)
scoreList = sorted(score.items())
count = 0
middle = cases / 2
i = 0
while count < middle:
    count += scoreList[i][1]
    i += 1
median = scoreList[i - 1][0]

# 범위 (최댓값 - 최솟값)
width = scoreList[-1][0] - scoreList[0][0]

# 최빈값 (개수 기준 : 내림차순, 점수 : 오름차순)
scoreList.sort(key=lambda x: x[1], reverse=True)
if len(scoreList) == 1:
    mode = scoreList[0][0]
elif scoreList[0][1] == scoreList[1][1]:
    mode = scoreList[1][0]
else:
    mode = scoreList[0][0]

# 결과 출력
print(average)
print(median)
print(mode)
print(width)
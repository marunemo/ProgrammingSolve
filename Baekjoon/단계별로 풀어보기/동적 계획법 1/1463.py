'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지이다.
    1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
    2. X가 2로 나누어 떨어지면, 2로 나눈다.
    3. 1을 뺀다.
'''
import sys

# 연산 횟수를 구할 n을 입력 받음
n = int(sys.stdin.readline())

# 0번째 인덱스는 인덱스를 해당 숫자와 동일하게 하기 위해 추가
calcCount = [0, 0]

# 2부터 n까지 총 연산 횟수를 구함(탑다운 알고리즘)
for i in range(2, n + 1):
    # 기본적으로 X는 (X - 1)번째의 연산 횟수 + 1로 계산 (연산 3. 이용)
    calcCount.append(calcCount[i - 1] + 1)

    # 만약 X가 3의 배수라면 해당 횟수 + 1로 계산 (연산 1. 이용)
    if i % 3 == 0 and calcCount[i] > calcCount[i // 3] + 1:
        calcCount[i] = calcCount[i // 3] + 1

    # 만약 x가 2의 배수라면 해당 횟수 + 1로 계산 (연산 2. 이용)
    if i % 2 == 0 and calcCount[i] > calcCount[i // 2] + 1:
        calcCount[i] = calcCount[i // 2] + 1

# n번째 인덱스의 최종 결과인 최소 연산 횟수를 출력
print(calcCount[n])
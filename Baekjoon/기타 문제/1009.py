'''
풀이

a^b의 형태로 값이 주어질 때, 10으로 나눈 나머지를 구하는 문제이다.
(1 ≤ a < 100, 1 ≤ b < 1,000,000)라는 범위가 주어져 있으므로, 직접 구하는 것에는 문제가 있다.

그렇기 때문에 a만큼을 b번 곱하는 방식으로 진행하되, 우리는 나머지를 중심으로 구해야 한다.
어떤 값에 x를 곱하고 10으로 나눈 값이 Q(x) + R(x)라고 할 때, Q(x)는 10으로 나누어 떨어지는 값인 몫,
R(x)는 10으로 나누어 떨어지지 않는 값, 즉 나머지라고 가정한다.
이때, x를 한 번 더 곱했을 때, xQ(x) + xR(x)에서 xQ(x)는 무조건 10으로 나누어 떨어지므로,
xR(x)에 대해서 10으로 한 번 더 나누고 나온 나머지가 2x 일때의 나머지가 된다.

따라서 1부터 시작하여 a를 곱하고 각 나머지를 10으로 나눈 나머지를 b회 반복하여 계산하면 된다.
이를 통해 예상했다시피, a가 1이거나 a가 10의 배수인 경우는 나머지가 각각 1과 0으로 고정된다는 점이 있다.
'''

# fast IO
from sys import stdin

# 테스트 케이스의 개수
t = int(stdin.readline())

# 각 테스트 케이스에 따른 a, b 값
dataAmount = []
for _ in range(t):
    a, b = map(int, stdin.readline().split())
    dataAmount.append([a, b])

# 각 테스트 케이스에 대해 마지막 데이터가 처리되는 컴퓨터의 번호를 출력
for a, b in dataAmount:
    lastCom = 1
    if a % 10 == 0:
        lastCom = 0
    elif a != 1:
        for _ in range(b):
            lastCom = (lastCom * a) % 10
    print(10 if lastCom == 0 else lastCom)
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

(1차 수정)
결국 10으로 나눈 나머지라는 것은 무엇을 해도 구구단처럼 일의 자리로만 이루어진 곱셈이라는 것이다.
게다가 컴퓨터의 번호는 그 일의 자리끼리의 곱에서도 결과가 일의 자리로만 나타내진다는 것이다.
일의 자리만 보자면 구구단은 다음과 같은 규칙을 따른다.
    1단) 1 -> 1 -> 1 -> ...
    2단) 2 -> 4 -> 8 -> 6 -> 2 -> ...
    3단) 3 -> 9 -> 7 -> 1 -> 3 -> ...
    4단) 4 -> 6 -> 4 -> ...
    5단) 5 -> 5 -> 5 -> ...
    6단) 6 -> 6 -> 6 -> ...
    7단) 7 -> 9 -> 3 -> 1 -> 7 -> ...
    8단) 8 -> 4 -> 2 -> 6 -> 8 -> ...
    9단) 9 -> 1 -> 9 -> ...
    10단) 0 -> 0 -> 0 -> ...
따라서 b의 값을 각 길이로 나눈 나머지의 인덱스를 a값의 일의 자리만의 리스트 중에 결정하면 된다.
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

# 일의 자리 리스트 생성
digitList = []
for i in range(10):
    digitLoop = [i]
    digit = (i * i) % 10
    while digit != i:
        digitLoop.append(digit)
        digit = (digit * i) % 10
    digitList.append(digitLoop)

# 각 테스트 케이스에 대해 마지막 데이터가 처리되는 컴퓨터의 번호를 출력
for a, b in dataAmount:
    digit = a % 10
    digitIndex = (b - 1) % len(digitList[digit])
    if digit == 0:
        print(10)
    else:
        print(digitList[digit][digitIndex])
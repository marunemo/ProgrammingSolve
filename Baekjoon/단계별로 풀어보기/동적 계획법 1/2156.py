'''
풀이

2579번 문제와 상당히 유사한 문제다.
이번에는 해당 문제와 다르게 풀어보려고 한다.

한 인덱스의 포도주를 반드시 마신다고 할 때, 세 잔을 연속으로 마시지 않고 해당 포도주를 마시는 방법은 두가지가 있다.
1. 현재 포도주와 인접하지 않은 잔을 마신다.
2. 현재 포도주와 인접한 하나의 잔을 마시되, 다음 잔은 해당 잔과 인접하지 않은 잔을 마신다.

이를 점화식으로 나타내면, 현재 인덱스를 n이라 할 때
해당 인덱스의 잔을 glass[n], 이전까지 마신 잔의 최댓값을 maxGlasses[n]이라고 한다면,
1. glass[n] + maxGlasses[n - 2]
2. glass[n] + glass[n - 1] + maxGlasses[n - 3]
이므로, maxGlasses[n]은 다음과 같이 표현할 수 있다.
maxGlasses[n] = max(glass[n] + maxGlasses[n - 2], glass[n] + glass[n - 1] + maxGlasses[n - 3])

이때, 마지막 잔을 꼭 마실 필요는 없으므로, 최댓값은 maxGlasses[n] 또는 maxGlasses[n - 1] 중에 있다.
(maxGlasses[n - 2]는 maxGlasses[n]이 glass[n] + maxGlasses[n - 2]를 포함하므로, glass[n]이 음이 아닌 정수인 이상
maxGlasses[n] >= maxGlasses[n - 2]를 항상 만족하기 때문에 고려하지 않아도 된다)
'''

# fast IO
from sys import stdin
input = stdin.readline

# 포도잔의 개수 입력
n = int(input())

# 각 잔에 따른 포도주의 양 입력
glass = []
for _ in range(n):
    wine = int(input())
    glass.append(wine)

# 마실 수 있는 포도주의 최댓값 계산
maxGlasses = []
for i in range(n):
    if i == 0:
        maxGlasses.append(glass[i])
    elif i == 1:
        maxGlasses.append(glass[i] + glass[i - 1])
    elif i == 2:
        maxGlasses.append(glass[i] + maxGlasses[i - 2])
    else:
        maxGlasses.append(max(glass[i] + maxGlasses[i - 2], glass[i] + glass[i - 1] + maxGlasses[i - 3]))

# 최대로 마실 수 있는 포도주의 양을 출력
print(max(maxGlasses[-2:]))
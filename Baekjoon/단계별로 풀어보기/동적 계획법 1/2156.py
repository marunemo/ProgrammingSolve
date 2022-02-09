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

=== 1차 수정 ===
2579번 문제 때문에 헷갈린 점이 있었다.
2579번 문제에서는 다음이나 다다음 계단으로 무조건 올라가야만 했으나, 여기서는 그렇지 않다는 점.
그렇지만 최댓값의 범위를 처음부터 n - 2까지로 정하기에는 무리가 있기에, 범위를 정할 필요가 있었다.
최댓값의 범위 n - 2와 n - 3은 각각 필요했고, n - 4까지도 고려할 필요가 있다.
예로 들어
ooxo...
xooxo..
ooxxo..
와 같은 상황에서는 2칸까지는 건너뛸 필요가 있었기 때문이다.
그러나 n - 5부터는 oxxxo와 같은 상황은 oxoxo가 다른 영향을 주지 않으면서도 항상 크거나 같은 값을 나타내므로,
n - 4라는 조건만 고려하면 된다.

이를 통해 우리가 나타낼 수 있는 경우는 다음과 같아진다.
1. oxo...
2. ooxo...
3. oxxo...
4. ooxxo...

결국 연속 여부를 고려하는 방향이 가장 적절할 것이다.
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
# 인덱스 0은 연속되지 않은 경우, 인덱스 1은 연속되는 경우를 의미
maxGlasses = []
for i in range(n):
    if i == 0:
        maxGlasses.append([glass[i], glass[i]])
    elif i == 1:
        maxGlasses.append([glass[i], glass[i] + glass[i - 1]])
    elif i == 2:
        continuousGlass = glass[i] + maxGlasses[i - 1][0]
        oneJumpGlass = glass[i] + max(maxGlasses[i - 2])
        maxGlasses.append([oneJumpGlass, continuousGlass])
    else:
        continuousGlass = glass[i] + maxGlasses[i - 1][0]
        oneJumpGlass = glass[i] + max(maxGlasses[i - 2])
        twoJumpGlass = glass[i] + max(maxGlasses[i - 3])
        maxGlasses.append([max(oneJumpGlass, twoJumpGlass), continuousGlass])

# 최대로 마실 수 있는 포도주의 양을 출력
lastGlass = max(maxGlasses[-1])
last2Glass = max(maxGlasses[-2])
print(max(lastGlass, last2Glass))
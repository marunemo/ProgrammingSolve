'''
풀이

DP의 대표적인 문제인 냅색 문제이다. (배낭 문제라고도 한다)
무게가 W이고, 가치가 V라고 할 때,
W의 합이 K 이하가 되도록 하면서 V의 합이 최대가 되도록 하는 결과를 찾으면 된다.

나는 바텀업을 사용하면 쉽게 풀릴 것이라 예상한다.
W의 범위가 (1 ≤ W ≤ 100,000)이므로, 처음을 0으로 초기화한 다음, 각각의 무게에 대한 최댓값을 구하면 될 것이라 예상한다.
'''

# fast IO
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
packing = {}
for _ in range(n):
    w, v = map(int, input().split())
    if w not in packing or packing[w] < v:
        packing[w] = v

for weight in range(1, k + 1):
    maxWeight = 0
    if weight in packing:
        maxWeight = packing[weight]
    for i in range(weight // 2 + 1):
        if i in packing and (weight - i) in packing:
            if maxWeight < packing[i] + packing[weight - i]:
                maxWeight = packing[i] + packing[weight - i]
    if maxWeight != 0:
        packing[weight] = maxWeight

print(packing[max(packing.keys())])
print(packing)
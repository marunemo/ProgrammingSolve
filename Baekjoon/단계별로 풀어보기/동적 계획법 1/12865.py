'''
풀이

DP의 대표적인 문제인 냅색 문제이다. (배낭 문제라고도 한다)
무게가 W이고, 가치가 V라고 할 때,
W의 합이 K 이하가 되도록 하면서 V의 합이 최대가 되도록 하는 결과를 찾으면 된다.

처음부터 각 무게들의 합으로 나타낼 수 있는 무게들의 최대 가치를 저장한다면 어떨까?

(1차 수정)
냅색 문제에 대한 이해가 필요하여 다음 사이트를 참고하였다.
(https://namu.wiki/w/%EB%B0%B0%EB%82%AD%20%EB%AC%B8%EC%A0%9C)
(https://www.youtube.com/watch?v=A8nOpWRXQrs)
'''

# 냅색 문제 알고리즘 (https://www.youtube.com/watch?v=A8nOpWRXQrs 참고)
def knapsack(index, maxWeight, packingItem):
    # 만약 아이템이 더이상 없거나 저장할 수 있는 무게가 없다면 취소
    if index < 0 or maxWeight <= 0:
        return 0
    
    # 무게와 가치를 불러옴
    weight, value = packingItem[index]

    # 만약 현재 인덱스의 무게가 최대 무게 이상이라면 다음 무게로 넘어감
    if weight > maxWeight:
        return knapsack(index - 1, maxWeight, packingItem)
    else:
        # 해당 인덱스의 물건을 포함하는 경우와 포함하지 않는 경우 중 최댓값을 반환
        notContainMax = knapsack(index - 1, maxWeight, packingItem)
        containMax = value + knapsack(index - 1, maxWeight - weight, packingItem)
        return max(notContainMax, containMax)

# fast IO
from sys import stdin
input = stdin.readline

# 물품의 수와 최대 무게를 입력
n, k = map(int, input().split())

# 각 물품들을 저장할 딕셔너리 생성
packing = []
for _ in range(n):
    w, v = map(int, input().split())
    packing.append([w, v])

# 가치의 합의 최댓값을 반환
print(knapsack(n - 1, k, packing))
'''
풀이

DP의 대표적인 문제인 냅색 문제이다. (배낭 문제라고도 한다)
무게가 W이고, 가치가 V라고 할 때,
W의 합이 K 이하가 되도록 하면서 V의 합이 최대가 되도록 하는 결과를 찾으면 된다.

처음부터 각 무게들의 합으로 나타낼 수 있는 무게들의 최대 가치를 저장한다면 어떨까?
'''

# fast IO
from sys import stdin
input = stdin.readline

# 물품의 수와 최대 무게를 입력
n, k = map(int, input().split())

# 각 물품들을 저장할 딕셔너리 생성
packing = {}
for _ in range(n):
    w, v = map(int, input().split())

    # 처음 들어가는 무게에 대하여 중복하여 세지 않도록 설정
    isdupl = False
    if w not in packing:
        packing[w] = v
        isdupl = True

    # 각 무게를 내림차순으로 정렬(계산된 무게가 뒤에서 한 번 더 계산되는 것을 방지)
    for i in sorted(packing.keys(), reverse=True):
        # 만약 현재 가치가 중복으로 계산될 수 있다면 계산하지 않음
        if isdupl and i == w:
            continue

        # 만약 해당 무게를 더했을 때에도 k값 이내라면, 가치의 최대값으로 수정
        if i + w <= k:
            if (i + w) not in packing or packing[i + w] < packing[i] + v:
                packing[i + w] = packing[i] + v
    
    # 해당 무게의 가치를 최대값으로 수정
    if packing[w] < v:
        packing[w] = v

# k에 가장 가까운 무게의 가치의 합을 출력
print(packing[max(packing.keys())])
'''
시간 초과로부터 벗어나기 위한 풀이
1. 홀수 + 홀수, 짝수 + 짝수는 모두 짝수로 2의 배수이므로, 홀수 + 짝수의 매치만 확인(최대 50개에서 최대 25개 씩으로 줄어듦)
2. 1.의 조건이 만족하기 위해서는 홀수와 짝수의 개수가 같아야 함
3. adjacency matrix 생성
4. 소수 쌍 재귀함수
'''

from math import sqrt
from sys import stdin

# 소수 판별 함수
def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 소수 쌍 생성 함수
def primePair(srcEdge, adjList, destIndex, isVisited):
    # 만약 현재 원소가 이미 방문되었다면 False를 출력
    # isVisited는 매 인덱스마다 초기화되며, 재귀로 인해 발생할 다음과 같은 상황을 방지한다.
    #   1. 첫 인덱스의 소수 쌍이 변경되는 것을 방지
    #   2. 재귀를 통해 같은 인덱스로 무한히 연결되는 것을 방지
    #   3. for문을 거친 뒤에도 False로 출력된 인덱스에 대해 다시 for문을 실행하는 것을 방지
    if isVisited[destIndex]:
        return False

    # 현재 원소가 방문된 것으로 설정
    isVisited[destIndex] = True

    # 현재 인덱스의 원소와의 합이 소수인 원소들 추출
    for srcIndex in adjList[destIndex]:
        # 만약 해당 원소가 아직 소수 쌍으로 연결되지 않았거나,
        # 이전까지 연결되었던 원소들이 현재의 소수 쌍 이외에는 다른 소수 쌍으로 나타낼 수 있을 경우에는
        # 현재 인덱스의 원소와 해당 원소를 연결하고 True를 출력 후 분기
        if srcIndex not in srcEdge or primePair(srcEdge, adjList, srcEdge[srcIndex], isVisited):
            srcEdge[srcIndex] = destIndex
            return True
    
    # 만약 현재 인덱스와의 합이 소수인 원소들이 모두 현재 인덱스와 소수 쌍을 이룰 수 없을 경우에는 False를 출력
    return False

# 수열의 길이와 수열 입력
numCount = int(stdin.readline())
numList = list(map(int, stdin.readline().split()))

# 결과를 출력할 리스트
resultList = []

# 수열의 홀수와 짝수를 분리
oddList, evenList = [], []
for num in numList:
    if num % 2 == 0:
        evenList.append(num)
    else:
        oddList.append(num)

# 홀수 수열과 짝수 수열의 예상 길이
maxRange = numCount // 2

# 인접리스트 생성
adjacencyList = [[] for _ in range(maxRange)]

# 만약 홀수와 짝수의 길이가 같을 경우에만 결과 값을 추출
if maxRange == len(oddList):
    # 기존 수열의 첫 원소가 있는 리스트를 destList로 설정
    if numList[0] % 2 == 0:
        destList, srcList = evenList, oddList
    else:
        destList, srcList = oddList, evenList
    
    # destList를 기준으로 합이 소수인 원소들에 대한 인접 리스트 저장
    for i in range(maxRange):
        for j in range(maxRange):
            if isPrime(destList[i] + srcList[j]):
                adjacencyList[i].append(j)

    # 첫 번째 원소와 연결된 합이 소수인 원소들 추출
    for pairedIndex in adjacencyList[0]:
        # 첫 번째 원소와 해당 원소를 연결 후, 연결된 개수를 초기화
        srcEdge = {pairedIndex : 0}
        pairedCount = 1

        # 첫 번째 원소가 포함된 리스트 중 첫 번째 원소를 제외한 원소들을 추출
        for i in range(1, maxRange):
            # 해당 원소의 방문 여부를 초기화한 후, 첫 번째 원소는 항상 연결된 것으로 설정(다른 원소에 의한 변경 방지)
            isVisited = {i : False for i in range(maxRange)}
            isVisited[0] = True

            # 현재 원소까지의 모든 원소들이 이분 매칭되었다면, 소수 쌍의 개수 추가
            if primePair(srcEdge, adjacencyList, i, isVisited):
                pairedCount += 1
        
        # 만약 모든 원소들이 연결되었다면, 첫 번째 원소와 연결된 원소를 결과 값에 추가
        if pairedCount == maxRange:
            resultList.append(srcList[pairedIndex])

# 결과 값 출력
if resultList:
    print(*sorted(resultList))
else:
    print(-1)
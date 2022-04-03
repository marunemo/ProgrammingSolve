'''
시간 초과로부터 벗어나기 위한 풀이
1. 홀수 + 홀수, 짝수 + 짝수는 모두 짝수로 2의 배수이므로, 홀수 + 짝수의 매치만 확인(최대 50개에서 최대 25개 씩으로 줄어듦)
2. 1.의 조건이 만족하기 위해서는 홀수와 짝수의 개수가 같아야 함
3. adjacency matrix 생성
'''

from math import sqrt
from sys import stdin

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primePair(destEdge, srcEdge, adjList, destIndex, isVisited):
    if isVisited[destIndex]:
        return False
    isVisited[destIndex] = True

    for srcIndex in adjList[destIndex]:
        if srcIndex not in srcEdge or primePair(destEdge, srcEdge, adjList, srcEdge[srcIndex], isVisited):
            destEdge[destIndex], srcEdge[srcIndex] = srcIndex, destIndex
            return True
    return False

numCount = int(stdin.readline())
numList = list(map(int, stdin.readline().split()))

oddList, evenList = [], []
for num in numList:
    if num % 2 == 0:
        evenList.append(num)
    else:
        oddList.append(num)

maxRange = numCount // 2
adjacencyList = [[] for _ in range(maxRange)]
resultList = []

if maxRange == len(oddList):
    if numList[0] % 2 == 0:
        destList, srcList = evenList, oddList
    else:
        destList, srcList = oddList, evenList
    
    for i in range(maxRange):
        for j in range(maxRange):
            if isPrime(destList[i] + srcList[j]):
                adjacencyList[i].append(j)

    for pairedIndex in adjacencyList[0]:
        destEdge, srcEdge = {0 : pairedIndex}, {pairedIndex : 0}
        pairedCount = 1
        for i in range(1, maxRange):
            isVisited = {i : False for i in range(maxRange)}
            isVisited[0] = True
            if primePair(destEdge, srcEdge, adjacencyList, i, isVisited):
                pairedCount += 1
        if pairedCount == maxRange:
            resultList.append(srcList[pairedIndex])

if resultList:
    print(*sorted(resultList))
else:
    print(-1)
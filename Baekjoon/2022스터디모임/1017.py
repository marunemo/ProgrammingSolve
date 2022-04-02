'''
시간 초과로부터 벗어나기 위한 풀이
1. 홀수 + 홀수, 짝수 + 짝수는 모두 짝수로 2의 배수이므로, 홀수 + 짝수의 매치만 확인(최대 50개에서 최대 25개 씩으로 줄어듦)
2. 1.의 조건이 만족하기 위해서는 홀수와 짝수의 개수가 같아야 함
'''

from math import sqrt
from sys import stdin

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primePair(destList, srcList, maxRange, destIndex, isVisited, resultList):
    if destIndex == maxRange:
        return True

    isAllMatched = False
    for srcIndex in range(maxRange):
        if not isVisited[srcIndex] and isPrime(destList[destIndex] + srcList[srcIndex]):
            isVisited[srcIndex] = True
            if primePair(destList, srcList, maxRange, destIndex + 1, isVisited, resultList):
                isAllMatched = True
                if destIndex == 0:
                    resultList.append(srcList[srcIndex])
            isVisited[srcIndex] = False
        
        if isAllMatched and destIndex != 0:
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

isVisited = {i : False for i in range(numCount // 2)}
maxRange = numCount // 2
resultList = []

if maxRange == len(oddList):
    if numList[0] % 2 == 0:
        destList, srcList = evenList, oddList
    else:
        destList, srcList = oddList, evenList
    primePair(destList, srcList, maxRange, 0, isVisited, resultList)

if resultList:
    print(*sorted(resultList))
else:
    print(-1)
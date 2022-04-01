from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primePair(numCount, numList, isVisited, firstIndex, resultPair):
    if firstIndex == numCount:
        return all(isVisited.values())

    if isVisited[firstIndex]:
        result = primePair(numCount, numList, isVisited, firstIndex + 1, resultPair)
        return result

    isVisited[firstIndex] = True

    isAllPaired = False
    for i in range(firstIndex + 1, numCount):
        if not isVisited[i]:
            if isPrime(numList[firstIndex] + numList[i]):
                isVisited[i] = True
                isAllPaired = primePair(numCount, numList, isVisited, firstIndex + 1, resultPair)
                isVisited[i] = False
                if isAllPaired:
                    if firstIndex == 0:
                        resultPair.append(numList[i])
                    else:
                        isVisited[firstIndex] = False
                        return isAllPaired
        isAllPaired = False

    isVisited[firstIndex] = False
    return isAllPaired

numCount = int(input())
numList = list(map(int, input().split()))

isVisited = {i : False for i in range(numCount)}
firstIndex = 0
resultPair = []

primePair(numCount, numList, isVisited, firstIndex, resultPair)
if resultPair:
    print(*sorted(resultPair))
else:
    print(-1)
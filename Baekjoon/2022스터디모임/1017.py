from math import sqrt
from sys import stdin

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primePair(numCount, numList, isVisited, adjacencyList, index):
    if index == numCount:
        return True

    if isVisited[index]:
        return primePair(numCount, numList, isVisited, adjacencyList, index + 1)
    
    isVisited[index] = True
    for vertex in adjacencyList[index]:
        if not isVisited[vertex]:
            isVisited[vertex] = True
            if primePair(numCount, numList, isVisited, adjacencyList, index + 1):
                isVisited[index] = False
                isVisited[vertex] = False
                return True
            isVisited[vertex] = False
    isVisited[index] = False
    return False
    

numCount = int(stdin.readline())
numList = list(map(int, stdin.readline().split()))

isVisited = {i : False for i in range(numCount)}

adjacencyList = {i : [] for i in range(numCount)}

for i in range(numCount):
    for j in range(i + 1, numCount):
        if isPrime(numList[i] + numList[j]):
            adjacencyList[i].append(j)

primeSet = []

isVisited[0] = True
for vertex in adjacencyList[0]:
    isVisited[vertex] = True
    if primePair(numCount, numList, isVisited, adjacencyList, 1):
        primeSet.append(numList[vertex])
    isVisited[vertex] = False

if primeSet:
    print(*sorted(primeSet))
else:
    print(-1)
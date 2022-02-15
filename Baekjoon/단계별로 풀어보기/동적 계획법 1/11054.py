'''
풀이

이전 문제인 11053번 문제의 LIS를 구하는 방법을 응용한다.
'''

# fast IO
from sys import stdin

# 수열 a의 크기와 수열 a를 입력받는다
sizeA = int(stdin.readline())
sequenceA = list(map(int, stdin.readline().split()))

# 수열의 증가를 탐색하는 리스트 생성
maxList = []
maxIndexList = []

# 수열의 감소를 탐색하는 리스트 생성
minList = []
minIndexList = []

# 바이토닉 수열의 증가 탐색
for i, a in enumerate(sequenceA):
    maxIndex = 0
    minIndex = 0

    while maxIndex < len(maxList) and a > maxList[maxIndex]:
        maxIndex += 1
    while minIndex < len(minList) and a < minList[minIndex]:
        minIndex += 1

    if maxIndex == len(maxList):
        maxList.append(a)
        maxIndexList.append(i)
    else:
        maxList[maxIndex] = a
        maxIndexList[maxIndex] = i

    if minIndex == len(minList):
        minList.append(a)
        minIndexList.append(i)
    else:
        minList[minIndex] = a
        minIndexList[minIndex] = i

maxLength = 0
for i in maxIndexList:
    while i > 

print(maxLength)
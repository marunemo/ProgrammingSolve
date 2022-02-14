'''
풀이

LIS가 무엇인가에 대해서는 다음을 참고하였다.
(https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4#rfn-1)
'''

# fast IO
from sys import stdin

# 수열 a의 크기와 수열 a를 입력받는다
sizeA = int(stdin.readline())
sequenceA = list(map(int, stdin.readline().split()))

# 마지막으로 큰 수를 저장하는 리스트 생성
maxList = []

# LIS의 증가 탐색
for a in sequenceA:
    i = 0
    while i < len(maxList) and a > maxList[i]:
        i += 1
    if i == len(maxList):
        maxList.append(a)
    else:
        maxList[i] = a

# 최장 증가 수열의 길이 출력
print(len(maxList))
'''
풀이

각 층을 가운데 정렬에서 좌측 정렬로 정리하자면,
대각선 왼쪽과 대각선 오른쪽은 현재 인덱스와 같거나 1 큰 인덱스로 나타낼 수 있다.
이를 거꾸로 나타내자면, 각 인덱스는 자신의 이전 줄의 현재 인덱스보다 1 작거나 같은 인덱스로부터 값을 인계받는다는 것이다.

이때, 값이 최대가 되야 하므로, 이전 줄에서 1 작은 인덱스와 같은 인덱스의 값을 서로 비교하여
최댓값을 골라 현재 값에 합치면 된다.
단, 각 줄마다 최대 인덱스가 1씩 증가하기 때문에,
마지막 인덱스는 현재 인덱스와 같은 이전 인덱스가 없으므로,
마지막 인덱스는 항상 (현재 인덱스 - 1)번째 인덱스의 값을 인계받는다.
'''

from sys import stdin
input = stdin.readline

# 삼각형의 크기
height = int(input())

# 삼각형의 각 층까지 만들어질 수 있는 최댓값
triangleSum = []

for level in range(height):
    # 각 줄에서의 삼각형의 숫자
    intList = list(map(int, input().split()))

    # 각 인덱스별 가능한 최댓값
    for i in range(level):
        if i == 0:
            intList[i] += triangleSum[i]
        elif i == level - 1:
            intList[i] += triangleSum[i - 1]
        else:
            if triangleSum[i - 1] > triangleSum[i]:
                intList[i] += triangleSum[i - 1]
            else:
                intList[i] += triangleSum[i]
    # 최댓값 인계
    triangleSum = intList

# 최댓값 출력
print(max(triangleSum))
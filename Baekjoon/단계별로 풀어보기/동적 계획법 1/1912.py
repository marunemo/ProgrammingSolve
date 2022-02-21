'''
풀이

결국 처음부터 시작해서 0보다 작지 않은 이상 연속해서 값을 더해간다.
그 과정에서 최댓값을 저장한다.
'''

# fast IO
from sys import stdin
input = stdin.readline

# 수열을 입력받는다.
n = int(input())
intList = list(map(int, input().split()))

# 수열의 연속합 중 최댓값을 탐색한다.
maxInt = intList[0]
listSum = 0
for i in intList:
    listSum += i
    if listSum > maxInt:
        maxInt = listSum
    if listSum < 0:
        listSum = 0

# 수열의 연속합 중 최댓값을 출력한다.
print(maxInt)
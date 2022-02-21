'''
풀이

1912.py와 동일한 풀이 방식이지만, dynamic programming 문제인 만큼 그에 맞는 풀이가 필요하다고 생각되었다.
'''

# fast IO
from sys import stdin
input = stdin.readline

# 수열을 입력받는다.
n = int(input())
intList = list(map(int, input().split()))

# 수열의 최댓값을 탐색한다.
maxInt = [intList[0]]
for i in intList[1:]:
    if i > i + maxInt[-1]:
        maxInt.append(i)
    else:
        maxInt.append(i + maxInt[-1])
    
# 수열의 최댓값을 출력한다.
print(max(maxInt))
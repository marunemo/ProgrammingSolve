'''
풀이

이전 문제인 11053번 문제의 LIS를 구하는 방법을 응용한다.
기본적인 풀이는 다음 블로그를 참고하였다.
(https://st-lab.tistory.com/136)
'''

# fast IO
from sys import stdin

# 수열 a의 크기와 수열 a를 입력받는다
sizeA = int(stdin.readline())
sequenceA = list(map(int, stdin.readline().split()))

# 수열의 증가를 탐색하는 리스트 생성
maxList = []

# 최장 증가 부분 수열
lis = []

# 수열의 감소를 탐색하는 리스트 생성
minList = []

# 최장 감소 부분 수열
lds = []

# 바이토닉 수열의 증가 탐색
for a in sequenceA:
    i = 0
    while i < len(maxList) and maxList[i] < a:
        i += 1
    
    if i == len(maxList):
        maxList.append(a)
    else:
        maxList[i] = a

    # 해당 인덱스에서의 최장 증가 부분 수열의 길이를 저장한다.
    # 이때, 인덱스는 0부터 계산되지만, 길이는 1부터 셈하므로 1을 더해준다.
    lis.append(i + 1)

# 바이토닉 수열의 감소 탐색(증가 탐색을 뒤에서부터 실행)
for a in sequenceA[::-1]:
    i = 0
    while i < len(minList) and minList[i] < a:
        i += 1
    
    if i == len(minList):
        minList.append(a)
    else:
        minList[i] = a
    lds.append(i + 1)
lds = lds[::-1]

# 각 길이를 합했을 때의 길이가 최장이 되는 경우 탐색
maxLength = 0
for i in range(sizeA):
    # 이때, lis는 해당 인덱스까지의 증가 수열을, lds는 해당 인덱스부터의 감소 수열을 의미하므로,
    # 해당 인덱스를 두 번 계산하게 된다. 따라서 길이 계산에 대해서는 1을 감소시킨다.
    bitonicLength = lis[i] + lds[i] - 1
    if maxLength < bitonicLength:
        maxLength = bitonicLength

# 최장 바이토닉 수열의 길이를 출력한다.
print(maxLength)
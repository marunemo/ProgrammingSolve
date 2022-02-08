'''
풀이

채널의 맨 처음 자리부터 끝까지 눌러본다.
만약 해당 버튼이 없다면, 그 버튼에 가장 가까운 크거나 작은 값으로 대체한다.
이때, 큰 값인 경우에는 그 뒤의 모든 번호를 누를 수 있는 최소 번호만으로 누르고,
작은 값인 경우에는 최대 번호만을 눌러 해당 채널에 가장 가깝게 설정해준다.
이후, 큰 값과 작은 값을 비교하여 가장 작은 값을 구한다.
(단, 한 자리가 작거나 큰 수도 고려한다.)

그리고 해당 값과 100으로부터의 차를 한 번 더 비교하여, 가장 작은 값을 출력한다.
'''

# fast IO
from sys import stdin
input = stdin.readline

# N, M, 고장난 버튼을 입력받는다.
n = input().rstrip()
m = int(input())
# M = 0인 경우 고장난 버튼을 입력받지 않는다.
if m == 0:
    brokenBtn = []
else:
    brokenBtn = list(map(int, input().split()))

if m == 9:
    # 누를 수 있는 채널이 없다면 +나 -로 이동하는 방법만 고려하면 된다.
    minCount = abs(int(n) - 100)
else:
    # 채널의 자리수와 누를 수 있는 버튼을 나열한다.
    channelLength = len(n)
    availableBtn = [i for i in range(10) if i not in brokenBtn]

    # 같은 자리의 수들 중 해당 채널에 가까운 크거나 작은 수들을 각각 구한다.
    smNearChannel = 0
    lgNearChannel = 0

    # 누를 수 없는 자리수가 나올 때까지 채널을 입력한다.
    isBroken = False
    for c in n:
        digitNum = int(c)
        # 만약 누를 수 없는 버튼이 이전에 나왔다면 큰 수의 경우 최솟값을, 작은 수의 경우 최댓값을 구한다.
        if isBroken:
            smNearChannel = smNearChannel * 10 + availableBtn[-1]
            lgNearChannel = lgNearChannel * 10 + availableBtn[0]
        # 만약 버튼을 누를 수 있다면 해당 버튼을 누른다.
        elif digitNum in availableBtn:
            smNearChannel = smNearChannel * 10 + digitNum
            lgNearChannel = lgNearChannel * 10 + digitNum
        # 만약 누를 수 없는 버튼이 있다면, 대신 그 버튼과 가장 가까이에 있는 버튼을 누른다.
        else:
            i = 0
            while availableBtn[i] < digitNum and i < len(availableBtn) - 1:
                i += 1
            if availableBtn[i] > digitNum:
                smNearChannel = smNearChannel * 10 + availableBtn[i - 1]
            else:
                smNearChannel = smNearChannel * 10 + availableBtn[i]
            lgNearChannel = lgNearChannel * 10 + availableBtn[i]
            isBroken = True

    # 채널의 자리수보다 1 크고 작은 채널도 고려한다.
    belowNearChannel = 0
    aboveNearChannel = 0

    # 이때, 자리수가 작은 채널은 최댓값을, 자리수가 큰 채널은 최솟값을 고려한다.
    for i in range(channelLength - 1):
        belowNearChannel = belowNearChannel * 10 + availableBtn[-1]
    for i in range(channelLength + 1):
        aboveNearChannel = aboveNearChannel * 10 + (availableBtn[0] if availableBtn[0] != 0 or len(n) == 1 else availableBtn[1])

    # 채널로부터의 떨어진 거리(+이나 -를 누르는 횟수)를 비교하여 최솟값을 출력한다.
    # 이때, 시작 채널인 100부터의 거리도 고려한다.
    n = int(n)
    availableCase = []
    availableCase.append(abs(n - smNearChannel) + channelLength)
    availableCase.append(abs(lgNearChannel - n) + channelLength)
    availableCase.append(abs(n - belowNearChannel) + (channelLength - 1))
    availableCase.append(abs(aboveNearChannel - n) + (channelLength + 1))
    availableCase.append(abs(n - 100))

    # 각 거리의 최솟값을 출력한다.
    minCount = min(availableCase)
print(minCount)
'''
풀이

계단을 밟는데 규칙은 다음과 같다.
    1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
    2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
    3. 마지막 도착 계단은 반드시 밟아야 한다.
결국 이를 정리하자면, 현재 위치를 기준으로 다음 혹은 다다음 번째 계단을 밟아야만 한다는 것인데,
세 계단을 연속으로 밟을 수 없다는 점을 바꿔 생각하면, 두 번의 계단을 밟을 때 중 한 번은 두 계단을 올라야 한다는 것이다.
즉, 이는 이전에 한 계단을 올라갔다면 그 다음은 무조건 두 계단을 올라가야 한다는 뜻이다.

여기서 중요한 것은 결국 세 번의 계단을 오르는 시행 중에는 반드시 한 번은 2칸을 밟는 경우가 필요하다는 것이다.
즉, 마지막을 2칸으로 마무리하는 시행들을 생각해보자면,
1. 2칸을 한 번에 오른다.
2. 한 칸을 오르고, 2칸을 한 번에 오른다.
로, 모든 계단을 오르는 시행은 해당 2가지 경우의 조합으로 나타낼 수 있다는 것이다.
다시 말해, 한 칸을 오를지 말지에 대하여 판단하기만 하면 된다는 것이다.

이를 코드로 나타내자면, 결국 중요한 것은 세 계단 중 2개를 필수적으로 선택한다는 것이다.
그리고 마지막 계단을 밟을 때까지 이를 반복한다.
'''

from sys import stdin
input = stdin.readline

stairs = int(input())

totalScore = 0
isContinuous = False
prePoint = 0
for i in range(stairs):
    point = int(input())
    if isContinuous:
        if prePoint < point:
            totalScore += point
        else:
            totalScore += prePoint
            isContinuous = False
    else:
        isContinuous = True
    prePoint = point

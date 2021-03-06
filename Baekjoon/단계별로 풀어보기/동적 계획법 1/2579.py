'''
풀이

계단을 밟는데 규칙은 다음과 같다.
    1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
    2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
    3. 마지막 도착 계단은 반드시 밟아야 한다.
결국 이를 정리하자면, 현재 위치를 기준으로 다음 혹은 다다음 번째 계단을 밟아야 하는데,
이때, 만약 바로 이전에 한 계단을 올랐다면, 다음 계단은 무조건 다다음 계단을 밟아야만 한다는 것이다.

예로 들어, 각 계단을 밟았다면 O, 밟지 않았다면 X라고 표기한다고 가정해보자.
그렇다면 4계단을 오르는 방법은 다음과 같다.
    1. oxox
    2. oxoo
    3. ooxo
    4. xoox
    5. xoxo
이를 통해 우리가 다시 알 수 있는 규칙은 다음과 같다.
    1. 하나의 계단을 중심으로 볼 때, 해당 계단을 밟는 방법과 밟지 않는 방법이 각각 최소한 하나 이상이 있다.
    2. 하나의 계단을 중심으로 볼 때, 해당 계단을 이전 계단에 연속되도록 밟는 방법과 연속되지 않도록 밟는 방법이 각각 최소한 하나 이상이 있다.
즉, 우리는 각 계단의 위치에 따라 해당 계단을 이전 계단에 연속되도록 밟는 방법과
연속되지 않도록 밟는 방법에 대해 최댓값을 모두 구할 수 있다는 것이다.
'''

# fastIO
from sys import stdin
input = stdin.readline

# 계단의 총 개수를 입력받는다.
stairs = int(input())

# 연속되는 계단의 최대 점수는 1번 인덱스에, 연속되지 않는 계단의 최대 점수는 0번 인덱스에 저장한다.
stairScore = [[0, 0] for _ in range(stairs)]

# 첫 계단의 점수는 균일하게 저장한다.
score = int(input())
stairScore[0] = [score, score]

# 두 번째 계단부터 다음과 같은 규칙이 적용된다.
# 연속되지 않으면 이전의 연속 여부는 무관하므로, 최댓값만 구한다.
# 연속인 경우에는 연속되지 않은 경우의 최댓값만 고려한다.
if stairs > 1:
    score = int(input())
    stairScore[1][0] = score
    stairScore[1][1] = score + stairScore[0][0]

    # 세 번째 계단부터 일정한 규칙이 반복된다.
    for i in range(2, stairs):
        score = int(input())
        stairScore[i][0] = score + max(stairScore[i - 2])
        stairScore[i][1] = score + stairScore[i - 1][0]

# 마지막 계단에서의 최댓값을 출력한다. (이때, 연속의 유무는 관계없다)
print(max(stairScore[stairs - 1]))
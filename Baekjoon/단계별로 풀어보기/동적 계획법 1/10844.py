'''
풀이

각 순열의 분기점의 개수를 그림으로 나타내본다면, 각 숫자가 나온 개수와 같다는 것을 알 수 있다.
이때, 각 순열은 인접한 자리의 1만큼의 차이가 나므로, ±1번째 숫자의 개수만 증가시키면 된다.
(단, 0과 9는 각각 +1, -1번째 숫자만 증가시킬 수 있으며, 첫 자리수는 0이 될 수 없다.)
'''

def calcStairCount(n, order, stairBranch):
    # 개수를 1,000,000,000으로 나눈 나머지를 반환한다.
    if order == n:
        return sum(stairBranch) % 1000000000

    # 각 자리 수의 ±1번째 수에 각 개수(분기)만큼을 더해준다.
    nextStairBranch = [0 for i in range(10)]
    for i in range(10):
        # -1이나 10은 한 자리 자연수가 아니므로, 포함하지 않는다.
        # 이때, 계산을 빠르게 하기 위해 1000000000을 나눈 나머지를 미리 계산한다.
        if i != 0:
            nextStairBranch[i - 1] += stairBranch[i] % 1000000000
        if i != 9:
            nextStairBranch[i + 1] += stairBranch[i] % 1000000000
    # 마지막 줄에서의 개수를 가져온다.
    return calcStairCount(n, order + 1, nextStairBranch)

# 처음 시작은 0을 제외한 모든 값이 1로 시작된다.
stairBranch = [0 if i == 0 else 1 for i in range(10)]

# N 값을 입력받는다.
n = int(input())
order = 0

# 정답을 출력한다.
print(calcStairCount(n, order + 1, stairBranch))
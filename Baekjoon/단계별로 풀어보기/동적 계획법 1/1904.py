'''
풀이

전반적인 풀이는 repetition을 포함한 순열이다.
우리는 크게 2가지로 묶을 수 있는데, 1과 00이다.
따라서, 1과 00으로 만들 수 있는 순열의 개수를 계산하면 된다.

이때, 중복이 있는 순열은 (수 묶음의 총 개수)! / (각 수 묶음의 개수)!로 계산되며,
00이라는 묶음이 하나 늘어날 때마다 수 묶음의 총 개수는 하나씩 줄어든다.

(1 / 28 수정)
맨 앞의 숫자를 1 또는 00으로 하면, 그 뒤의 수열은 각각 길이가 (n - 1), (n - 2)인 수열로 나타낼 수 있다.
이를 이산수학에서의 재귀적 귀납법으로 증명한다면 다음과 같다.
f(1) = 1, f(2) = 2 (00, 11)
f(n) = (1) ^ f(n - 1) + (00) ^ f(n - 2)
이때, f(n - 2)는 n이 1 또는 2 모두에 도달 가능하므로, f(n)은 존재한다.
'''

# 타일 가짓수 탐색
def countTile(n):
    a, b = 1, 2
    for i in range(n - 1):
        a, b = b, a + b
    return a

# 타일의 길이 입력
n = int(input())

# 이진 수열의 개수를 15746으로 나눈 나머지 출력
print(countTile(n) % 15746)
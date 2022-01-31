'''
풀이

나선 삼각형에서 가장 긴 변을 한 변으로 하는 정삼각형을 만들어나간다고 할 때, 다음과 같은 규칙을 띤다.
P(1) = 1, P(2) = 1, P(3) = 1
P(n) = P(n - 2) + P(n - 3) --- (n > 3)

이는 P(n) = P(n - 2) + P(n - 3) --- (n > 3)가 참이라고 할 때, 다음과 같이 증명할 수 있다.
P(1)부터 P(5)까지는 1, 1, 1, 2, 2의 순열을 따른다.
n > 5일때, P(n)은 n을 2로 나눈 나머지가 같은 수끼리 방향을 공유하고,
P(n)과 p(n - 4)끼리 서로 인접하므로, P(n) = P(n - 1) + P(n - 5)가 된다.
여기서 조금 변형하면,
P(n) = P(n - 1) + P(n - 5) = P(n - 2) + P(n - 6) + P(n - 5)
k = n - 3일때,
P(n) = P(n - 2) + P(k - 3) + P(k - 2)
= P(n - 2) + P(k)
= P(n) = P(n - 2) + P(n - 3)이 된다.
이때, P(5) = P(3) + P(2), P(4) = P(2) + P(1)을 따르므로, 위 전제는 참이다.
'''

from sys import stdin
input = stdin.readline

def padovanSequence(n):
    a, b, c = 1, 1, 1
    for _ in range(n - 1):
        a, b, c = b, c, a + b
    return a

testcase = int(input())
n = []
for _ in range(testcase):
    n.append(int(input()))

for i in n:
    print(padovanSequence(i))
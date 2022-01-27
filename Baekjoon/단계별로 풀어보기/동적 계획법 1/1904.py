'''
풀이

전반적인 풀이는 repetition을 포함한 순열이다.
우리는 크게 2가지로 묶을 수 있는데, 1과 00이다.
따라서, 1과 00으로 만들 수 있는 순열의 개수를 계산하면 된다.

이때, 중복이 있는 순열은 (수 묶음의 총 개수)! / (각 수 묶음의 개수)!로 계산되며,
00이라는 묶음이 하나 늘어날 때마다 수 묶음의 총 개수는 하나씩 줄어든다.
'''

# 팩토리얼 재귀 함수 생성
def factorial(n):
    global factorialList
    if n not in factorialList:
        factorialList[n] = n * factorial(n - 1)
    return factorialList[n]

# 메모이제이션
factorialList = {0 : 1, 1 : 1}

# 타일의 길이 입력
n = int(input())

total = 0
for i in range(n):
    if n < 2*i:
        break
    # 전체 길이가 1씩 감소하고, 해당 전체 길이에 각 중복의 개수가 1씩 증감한다.
    total += factorial(n - i) // (factorial(i) * factorial(n - i - i))

# 이진 수열의 개수를 15746으로 나눈 나머지 출력
print(total % 15746)
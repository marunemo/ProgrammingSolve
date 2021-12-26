# 필요한 시간의 합
answer = 0

# 사람 수 입력
cases = int(input())

# 인출 시간
takeMoney = list(map(int, input().split()))

# 인출 시간 정렬 (각 사람이 인출하는 데 필요한 시간 최소화)
takeMoney.sort()

# 각 사람의 인출할 때 필요한 시간의 합 계산
totalTime = 0
for i in takeMoney:
    totalTime += i
    answer += totalTime

# 필요한 시간의 합 출력
print(answer)
# 최좌단 도시부터 최우단 도시까지 가는 최소 비용
answer = 0

# 도시 개수 입력
cityCount = int(input())

# 도로 길이 입력
roadLines = list(map(int, input().split()))

# 주유소 리터당 가격 입력
pricePerLiter = list(map(int, input().split()))

# 가장 싼 주유소 가격
minPrice = pricePerLiter[0]

# 각 도시까지의 최소 비용 계산 (가장 오른쪽의 도시의 가격은 고려하지 않음)
for i in range(cityCount - 1):
    if minPrice > pricePerLiter[i]:
        minPrice = pricePerLiter[i]
    answer += minPrice * roadLines[i]

# 최소 비용 출력
print(answer)
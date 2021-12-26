# 필요한 동전의 총 개수
answer = 0

# 동전의 개수와 가치의 합 입력
coins, price = map(int, input().split())

# 각 동전의 가치 입력
coin = []
for _ in range(coins):
    coin.append(int(input()))

# 각 동전의 크기를 큰 수부터 감산
i = len(coin) - 1

# 가치의 합이 맞아 떨어질 때까지 반복
while price != 0:
    if coin[i] <= price:
        answer += price // coin[i]
        price %= coin[i]
    i -= 1

# 총 개수 출력
print(answer)
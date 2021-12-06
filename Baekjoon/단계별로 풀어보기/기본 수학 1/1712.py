fixed, variable, price = map(int, input().split())

# n개 생산 시, 비용 = (고정 비용) + (가변 비용) * n, 이익 = (판매 비용) * n
# 이때, 이익 > 비용인 시점은 (판매 비용) * n > (고정 비용) + (가변 비용) * n
# 따라서 n > (고정 비용) / ((판매 비용) - (가변 비용))일 때, 손익분기

if price == variable:
    print("-1")
else:
    margin = fixed / (price - variable)
    if margin <= 0:
        print("-1")
    else:
        print(int(margin) + 1)
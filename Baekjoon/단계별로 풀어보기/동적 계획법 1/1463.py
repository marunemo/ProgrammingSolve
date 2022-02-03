def calcX(x):
    # x가 1이 되었을 때부터 연산 횟수를 세기 시작한다.
    if x == 1:
        return 0

    # 각 경우의 최솟값을 구한다.
    count = []

    # x가 3으로 나누어 떨어지면 3의 배수가 아닐 때까지 3으로 나누고, 해당 횟수를 더한다.
    if x % 3 == 0:
        mod3 = x
        mod3Cnt = 0
        while mod3 % 3 == 0:
            mod3 //= 3
            mod3Cnt += 1
        count.append(calcX(mod3) + mod3Cnt)

    # x가 2으로 나누어 떨어지면 2의 배수가 아닐 때까지 2으로 나누고, 해당 횟수를 더한다.
    if x % 2 == 0:
        mod2 = x
        mod2Cnt = 0
        while mod2 % 2 == 0:
            mod2 //= 2
            mod2Cnt += 1
        count.append(calcX(x // 2) + 1)

    # x를 1로 뺐을 때 3이나 2의 배수가 아니라면, 연산 횟수를 크게 줄이지 못하므로 무시한다.
    x -= 1
    if x % 3 == 0 or x % 2 == 0:
        count.append(calcX(x) + 1)
    
    # 짝수는 x 또는 x - 1 중 하나에 반드시 존재하므로, count가 빈 리스트가 될 수는 없다.
    return min(count)

# n을 입력받아 연산 횟수를 출력한다.
n = int(input())
print(calcX(n))
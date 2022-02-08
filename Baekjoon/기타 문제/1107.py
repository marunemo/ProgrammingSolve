'''
풀이

처음부터 brute force로 풀면 되는 거를 괜히 꼼수부리려다가 6번이나 틀렸다.
'''

def findButton(order, channel, length, n, availableBtn):
    if order == length:
        return channel
    
    minNum = 5000001
    minChannel = 0
    for i in availableBtn:
        currChannel = findButton(order + 1, channel * 10 + i, length, n, availableBtn)
        if minNum > abs(n - currChannel):
            minNum = abs(n - currChannel)
            minChannel = currChannel
    return minChannel

n = int(input())
m = int(input())
if m == 0:
    brokenBtn = []
else:
    brokenBtn = list(map(int, input().split()))

if m == 10:
    print(abs(n - 100))
else:
    availableBtn = [i for i in range(10) if i not in brokenBtn]

    availableCase = [abs(n - 100)]
    for i in range(1, 7):
        btnCount = findButton(0, 0, i, n, availableBtn)
        availableCase.append(abs(n - btnCount) + i)
    print(min(availableCase))
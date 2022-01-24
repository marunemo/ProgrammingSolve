def embedOperatorMax(numberList, operatorLimit, operatorCount, order, n, result):
    if order == n:
        return result
    
    totalResult = []
    for i in range(4):
        if operatorLimit[i] != operatorCount[i]:
            operatorCount[i] += 1
            if i == 0:
                totalResult.append(embedOperatorMax(numberList, operatorLimit, operatorCount, order + 1, n, result + numberList[order]))
            elif i == 1:
                totalResult.append(embedOperatorMax(numberList, operatorLimit, operatorCount, order + 1, n, result - numberList[order]))
            elif i == 2:
                totalResult.append(embedOperatorMax(numberList, operatorLimit, operatorCount, order + 1, n, result * numberList[order]))
            else:
                totalResult.append(embedOperatorMax(numberList, operatorLimit, operatorCount, order + 1, n, int(result / numberList[order])))
            operatorCount[i] -= 1
    return max(totalResult)

def embedOperatorMin(numberList, operatorLimit, operatorCount, order, n, result):
    if order == n:
        return result
    
    totalResult = []
    for i in range(4):
        if operatorLimit[i] != operatorCount[i]:
            operatorCount[i] += 1
            if i == 0:
                totalResult.append(embedOperatorMin(numberList, operatorLimit, operatorCount, order + 1, n, result + numberList[order]))
            elif i == 1:
                totalResult.append(embedOperatorMin(numberList, operatorLimit, operatorCount, order + 1, n, result - numberList[order]))
            elif i == 2:
                totalResult.append(embedOperatorMin(numberList, operatorLimit, operatorCount, order + 1, n, result * numberList[order]))
            else:
                totalResult.append(embedOperatorMin(numberList, operatorLimit, operatorCount, order + 1, n, int(result / numberList[order])))
            operatorCount[i] -= 1
    return min(totalResult)

n = int(input())
numberList = list(map(int, input().split()))
operatorLimit = list(map(int, input().split()))
operatorCount = [0] * 4
order = 0

maxCalc = embedOperatorMax(numberList[1:], operatorLimit, operatorCount, order, n - 1, numberList[0])
minCalc = embedOperatorMin(numberList[1:], operatorLimit, operatorCount, order, n - 1, numberList[0])

print(maxCalc)
print(minCalc)
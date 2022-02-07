scoreLog = input()
scoreChart = [[0, 1] for _ in range(23)]
frame = 0
isSecond = False
for i, log in enumerate(scoreLog):
    if log == "S":
        point = 10
        if frame < 9:
            scoreChart[i + 1][1] += 1
            scoreChart[i + 2][1] += 1
            isSecond = True
    elif log == "P":
        point = 10 - scoreChart[i - 1][0]
        if frame < 9:
            scoreChart[i + 1][1] += 1
    elif log == "-":
        point = 0
    else:
        point = int(log)
    scoreChart[i][0] = point
    if isSecond:
        frame += 1
    isSecond = not isSecond

totalScore = 0
for score, bonus in scoreChart:
    totalScore += score * bonus
print(totalScore)
'''
풀이

기존 풀이대로 풀어보기로 해보았다.
'''

# fast IO
from sys import stdin
input = stdin.readline

numCount = int(input())

randomSeq = [int(input()) for _ in range(numCount)]

stack = []
maxTop = 0

operationResult = ""

for num in randomSeq:
    if num > maxTop:
        while num > maxTop:
            maxTop += 1
            stack.append(maxTop)
            operationResult += "+"

    top = stack.pop()
    if top == num:
        operationResult += "-"
    else:
        operationResult = "NO"
        break

if operationResult == "NO":
    print("NO")
else:
    for oper in operationResult:
        print(oper)
# 식 입력
formula = input()

# '-' 전후로 괄호 생성(모든 + 를 -로 변경)
formula = formula.split('-')

# 결과 값
answer = sum(map(int, formula[0].split('+')))
for sub in formula[1:]:
    answer -= sum(map(int, sub.split('+')))

# 최솟값 출력
print(answer)
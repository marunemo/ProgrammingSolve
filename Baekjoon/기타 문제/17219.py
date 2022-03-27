'''
풀이

이 문제에서 가장 중요한 것은 사이트와 비밀번호를 매핑하는 것, 그리고 저장과 탐색을 효율적으로 하는 방법을 생각하는 것이다.
그 외에는 따로 생각할 요소가 없는 간단한 문제이다.
'''

# fast IO
from sys import stdin
input = stdin.readline

# 저장할 사이트 주소와 비밀번호의 수와 비밀번호를 찾을 사이트의 수를 입력
siteCount, searchCount = map(int, input().split())

# 사이트와 비밀번호 매핑
sitePwd = {}
for _ in range(siteCount):
    site, pwd = input().split()
    sitePwd[site] = pwd

# 사이트의 비밀번호를 저장
searchedPwd = []
for _ in range(searchCount):
    searchSite = input().strip()
    searchedPwd.append(sitePwd[searchSite])

# 사이트 별 비밀번호 출력
for pwd in searchedPwd:
    print(pwd)
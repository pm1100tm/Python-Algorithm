"""
완전수 구하기

자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다.
예를 들면, 6과 28은 완전수이다. 6=1+2+3 // 1,2,3은 각각 6의 약수 28=1+2+4+7+14 // 1,2,4,7,14는 각각 28의 약수
입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드를 작성하라.
"""

n = 10000
submultiple = []

for i in range(1, n+1):
    for j in range(1, i):
        if i != j and i % j == 0:
            submultiple.append(j)
    if sum(submultiple) == i:
        print(i)
    submultiple.clear()

# 6
# 28
# 496
# 8128
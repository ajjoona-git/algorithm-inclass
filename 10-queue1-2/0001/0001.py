# 0001. 부분 집합

from itertools import combinations

arr = list(range(1, 11))
result = []

# 모든 길이의 조합을 고려한다.
for r in range(1, 11):
    powersets = list(combinations(arr, r))
    # 생성한 부분집합을 순회하면서 합이 10이면 result에 추가한다.
    for powerset in powersets:
        if sum(powerset) == 10:
            result.append(powerset)

# 결과를 출력한다.
while result:
    print(*result.pop())
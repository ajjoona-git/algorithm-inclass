# 4012. 요리사

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # arr: 시너지 S_ij의 값
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 맛의 차이
    min_diff = float('inf')

    # 식재료 n//2개를 택하는 모든 조합 (nC2)
    for group_a in combinations(range(N), N//2):
        # synergy: 식재료를 택했을 때 시너지의 합
        # 0번 인덱스는 A음식의 맛, 1번 인덱스는 B음식의 맛
        synergy = [0] * 2

        # A음식에서 각 재료들의 시너지
        for i, j in combinations(group_a, 2):
            synergy[0] += arr[i][j] + arr[j][i]
        
        # 남은 재료는 B음식을 만든다.
        # group_b = []
        # for i in range(N):
        #     if i not in group_a:
        #         group_b.append(i)
        group_b = [i for i in range(N) if i not in group_a]
        
        # B음식에서 각 재료들의 시너지
        for i, j in combinations(group_b, 2):
            synergy[1] += arr[i][j] + arr[j][i]

        # 맛의 차이의 최소값을 갱신한다.
        min_diff = min(min_diff, abs(synergy[0] - synergy[1]))

    print(f'#{tc} {min_diff}')
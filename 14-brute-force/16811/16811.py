# 16811. 당근 포장하기
# 7/20 제한 시간 초과

from itertools import combinations


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    min_diff = float('inf')

    # 대/중/소 그룹을 구분할 칸막이의 인덱스
    for idx_1, idx_2 in combinations(range(1, N), 2):
        len_s1 = idx_1
        len_s2 = idx_2 - idx_1
        len_s3 = N - idx_2
        max_len = max(len_s1, len_s2, len_s3)

        # 1. 한 상자에 당근의 수는 N//2를 초과하면 안 된다. (len() <= N//2)
        if max_len > N // 2:
            continue

        s1 = set(carrots[:idx_1])
        s2 = set(carrots[idx_1:idx_2])
        s3 = set(carrots[idx_2:])

        # 2. 같은 크기의 당근은 같은 상자에 들어있어야 한다. (교집합 != {})
        if s1.intersection(s2) or s2.intersection(s3):
            continue

        # 개수 차이 갱신
        min_len = min(len_s1, len_s2, len_s3)
        min_diff = min(min_diff, max_len - min_len)

    # 포장 할 수 없는 경우 -1, 포장할 수 있으면 상자에 들어있는 당근의 개수 차이가 최소일 때의 차이값
    if min_diff == float('inf'):
        result = -1
    # 포장할 수 있으면 상자에 들어있는 당근의 개수 차이가 최소일 때의 차이값
    else:
        result = min_diff

    print(f'#{tc} {result}')

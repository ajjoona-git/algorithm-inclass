# 1486. 장훈이의 높은 선반


def sum_heights(i, curr_height):
    """현재 높이의 인덱스(i)를 시작으로 재귀 호출(DFS)하면서 높이를 합산해간다."""
    global min_diff

    # 종료 조건: 높이가 B 이상인 경우, 최소 높이 차를 갱신한다.
    # return을 통해 높이가 B 이상이면 더 이상 높이를 합산하지 않는다.(가지치기)
    if curr_height >= B:
        min_diff = min(min_diff, (curr_height - B))
        return
    
    # 남아있는 인덱스들을 순회하면서 높이를 합산한다.
    for next_idx in range(i + 1, N):
        sum_heights(next_idx, curr_height + heights[next_idx])


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    
    min_diff = sum(heights)
    for i in range(N):
        sum_heights(i, heights[i])

    print(f'#{tc} {min_diff}')
# 5189. 전자카트


def minimum_path(start, cnt, total):
    global result

    # 종료조건: 모든 관리구역(N-1개)을 방문했다면 사무실로 복귀 후 최소값 갱신
    if cnt == N - 1:
        total += cost[start][1]
        result = min(result, total)
        return

    # 가지치기
    if total >= result:
        return

    # 방문하지 않은 관리구역 방문
    for next_node in range(2, N+1):
        if not visited[next_node]:
            visited[next_node] = True
            minimum_path(next_node, cnt + 1, total + cost[start][next_node])
            visited[next_node] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 0 인덱스는 사용하지 않는다.
    cost = [[0] + list(map(int, input().split())) for _ in range(N)]
    cost.insert(0, [0] * (N + 1))
    # 관리구역의 방문여부 (0,1 인덱스는 사용하지 않는다.)
    visited = [False] * (N + 1)

    result = float('inf')
    minimum_path(1, 0, 0)

    print(f'#{tc} {result}')

# 5102. 노드의 거리

from collections import deque


def bfs(s, g):
    visited = [0] * (V + 1)
    q = deque()

    visited[s] = 1
    q.append(s)

    while q:
        current_node = q.popleft()

        for next_node in adj_list[current_node]:
            if visited[next_node] == 0:
                visited[next_node] = visited[current_node] + 1
                q.append(next_node)

            if next_node == g:
                return visited[g] - 1
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    # 출발 노드 S, 도착 노드 G
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G)}')

# 연습문제. BFS
from collections import deque

def bfs(start_node, path=[]):
    """start_node부터 시작하여 BFS 방식으로 탐색하는 함수"""
    q = deque()

    visited[start_node] = True
    q.append(start_node)
    
    while q:
        current_node = q.popleft()
        path.append(current_node)

        for next_node in adj_list[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
    
    return path


V, E = map(int, input().split())
edge_info = list(map(int, input().split()))
visited = [False] * (V + 1)

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = edge_info[i * 2], edge_info[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

result = bfs(1)
print(''.join(map(str, result)))
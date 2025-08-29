# 연습문제. DFS

def dfs(start_node, path=[]):
    """start_node부터 시작하여 DFS 방식으로 재귀 호출하며 탐색하는 함수"""
    visited[start_node] = True
    path.append(start_node)

    for next_node in adj_list[start_node]:
        if not visited[next_node]:
            dfs(next_node, path)

    return path


V, E = map(int, input().split())
edge_info = list(map(int, input().split()))
visited = [False] * (V + 1)

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = edge_info[i * 2], edge_info[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

result = dfs(1)
print(''.join(map(str, result)))
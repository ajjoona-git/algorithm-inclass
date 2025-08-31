# 1267. 작업 순서


def dfs(curr_node):
    """curr_node 노드부터 시작해서 dfs방식으로 탐색"""
    visited[curr_node] = True
    
    # 후행 노드들에 대해서 방문하지 않았다면 재귀 호출
    for next_node in adj_list[curr_node]:
        if not visited[next_node]:
            dfs(next_node)
    
    # 재귀 호출이 모두 끝났다면 현재 노드는 할 수 있는 가장 마지막 작업이기 때문에
    # 작업 순서 상으로는 가장 앞에 추가한다.
    # 그래야 남은 작업들이 작업 순서 상 현재 작업보다 더 앞에 위치할 수 있다.
    result = [curr_node] + result
    


T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge_info = list(map(int, input().split()))

    adj_list = [[] for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = edge_info[i * 2], edge_info[i * 2 + 1]
        adj_list[n1].append(n2)
    
    visited = [False] * (V + 1)
    result = []

    for node in range(1, V + 1):
        # 방문하지 않았다면, 탐색 진행
        if not visited[node]:
            dfs(node)
    
    print(f'#{tc}', *result)
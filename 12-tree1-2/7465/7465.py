# 7465. 창용 마을 무리의 개수 


def dfs(start):
    """start부터 시작해서 DFS로 탐색한 노드를 모두 방문 처리하는 함수"""
    visited[start] = True
    stack = [start]

    while stack:
        current_node = stack.pop()
        
        for next_node in adj_list[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)


T = int(input())
for tc in range(1, T+1):
    # N명, M개의 관계
    N, M = map(int, input().split())
    
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    # 무리의 수를 세기 위한 초기 설정
    group_count = 0
    visited = [False] * (N + 1)

    # 1번 사람부터 연결된 무리를 방문 체크한다.
    # (0번 인덱스는 사용하지 않는다.)
    for i in range(1, N + 1):
        # 방문하지 않았다면, 새로운 무리의 시작
        # 무리에 속한 사람들을 모두 방문 처리한다.
        if not visited[i]:
            group_count += 1
            dfs(i)
    
    print(f'#{tc} {group_count}')
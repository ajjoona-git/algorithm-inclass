# 1248. 공통조상

import sys
sys.stdin = open("input.txt")


def dfs_count(start):
    """start부터 시작해서 DFS로 탐색한 노드의 개수 반환하는 함수"""
    visited = [False] * (V + 1)
    count = 0

    visited[start] = True
    stack = [start]
    
    while stack:
        current_node = stack.pop()
        count += 1

        for next_node in children[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
    
    return count


def find_ancestor(node):
    """node의 조상 노드들을 set 형태로 반환하는 함수"""
    ancestors = set()

    # 부모 노드가 없을 때까지 반복
    while parents[node] != 0:
        node = parents[node]
        ancestors.add(node)
    
    return ancestors



T = int(input())
for tc in range(1, T+1):
    V, E, N1, N2 = map(int, input().split())
    edge_list = list(map(int, input().split()))
    
    # 자식 노드 번호를 인덱스로, 부모 노드 번호를 저장
    parents = [0] * (V + 1)
    # 부모 노드 번호를 인덱스로, 자식 노드 번호를 저장
    children = [[] for _ in range(V + 1)]

    for i in range(E):
        parent, child = edge_list[i * 2], edge_list[i * 2 + 1]

        parents[child] = parent
        children[parent].append(child)

    # 노드부터 루트 노드까지의 경로를 세트로 저장한다.
    n1_ancs = find_ancestor(N1)
    n2_ancs = find_ancestor(N2)
    
    # 두 정점의 조상 리스트 중에 공통 조상 번호 중 가장 큰 값
    common_ancs = max(n1_ancs.intersection(n2_ancs))

    # common_ancs의 서브 트리의 길이를 구한다.
    subtree_size = dfs_count(common_ancs)
    print(f'#{tc} {common_ancs} {subtree_size}')
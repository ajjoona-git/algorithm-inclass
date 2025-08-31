# 1248. 공통조상

# import sys
# sys.stdin = open("input.txt")


def dfs_count(start):
    """start부터 시작해서 DFS로 탐색한 서브트리의 노드의 개수를 반환하는 함수"""
    visited = set()

    visited.add(start)
    stack = [start]
    
    while stack:
        current_node = stack.pop()

        for next_node in children[current_node]:
            if next_node not in visited:
                visited.add(next_node)
                stack.append(next_node)
    
    return len(visited)


def find_ancestor(node):
    """node의 조상 노드들을 list 형태로 반환하는 함수"""
    ancestors = []

    # 부모 노드가 없을 때까지 반복
    while parents[node] != 0:
        node = parents[node]
        ancestors.append(node)
    
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
    
    # 두 정점의 조상 리스트 중에 공통 조상 번호 중 가장 가까운 값
    # 노드번호는 크기순이 아니므로, 인덱스가 작은 값이 가장 가까운 값이다.
    # common_ancs = max(n1_ancs.intersection(n2_ancs))
    for n1_anc in n1_ancs:
        if n1_anc in n2_ancs:
            common_ancs = n1_anc
            break

    # common_ancs의 서브 트리의 길이를 구한다.
    subtree_size = dfs_count(common_ancs)
    print(f'#{tc} {common_ancs} {subtree_size}')
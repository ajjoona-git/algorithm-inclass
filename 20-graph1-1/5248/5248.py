# 5248. 그룹 나누기 

def find_set(x):
    """경로 압축 기법) 대표 원소를 찾는다."""
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    """랭크 기반 통합) 트리의 높이가 더 높은 그룹 밑에 낮은 그룹을 붙인다."""
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return
    
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    apply = list(map(int, input().split()))

    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    for i in range(M):
        v1, v2 = apply[i * 2], apply[i * 2 + 1]
        union(v1, v2)

    representatives = set()
    for i in range(1, N + 1):
        representatives.add(find_set(i))
    
    print(f'#{tc} {len(representatives)}')
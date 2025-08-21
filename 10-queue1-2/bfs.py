"""
input:
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
"""

def bfs(s, V):
    """
    너비 우선 탐색
    s: 시작 정점, V: 정점의 수
    """
    # 1. 초기화
    # 1-1. visited 생성: 여기서는 그래프의 깊이(계층)를 의미한다.
    # (s는 1, 그 다음 자식 노드는 2, ...)
    visited = [0] * (V + 1)
    # 1-2. 큐 생성, 시작점 인큐
    q = [s]
    # 1-3. 시작점 인큐(방문) 표시
    visited[s] = 1

    # 2. 반복
    # 탐색할 정점이 남아 있는 동안 반복한다.
    while q:
        # 2-1. 디큐
        t = q.pop(0)
        # 2-2. visit(): 여기서는 방문 정점 출력
        print(t, end=' ')
        # 2-3. 인접한 정점 순회
        for w in adj_lst[t]:
            # 2-4. 미방문인 경우 인큐, 인큐(방문) 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    return


# V: 정점의 수, E: 간선의 수
V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트(방향 표시가 없는 경우)
# V번째 행까지 준비
adj_lst = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2 + 1]
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1)

bfs(1, V)  # 1 2 3 4 5 7 6 
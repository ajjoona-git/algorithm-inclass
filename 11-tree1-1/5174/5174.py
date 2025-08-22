# 5174. subtree

def preorder(node):
    """주어진 노드 번호(node)를 루트로 하는 서브 트리를 전위순회(VLR)하면서 노드의 개수를 +1한다."""
    global cnt_node
    if node != 0:
        cnt_node += 1
        preorder(left[node])
        preorder(right[node])


T = int(input())
for tc in range(1, T+1):
    # E: 간선의 수, N: 찾고자하는 루트 노드
    E, N = map(int, input().split())
    # V: 노드의 수
    V = E + 1

    # 간선 정보 (부모, 자식) 쌍
    edge = list(map(int, input().split()))

    # 자식 리스트
    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for i in range(E):
        parent, child = edge[2*i], edge[2*i + 1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child
    
    cnt_node = 0
    preorder(N)

    print(f'#{tc} {cnt_node}')
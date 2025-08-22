# 0000. 순회

def preorder(node):
    """트리를 전위 순회(VLR)하면서 정점의 번호를 출력한다."""
    if node != 0:
        print(node, end=' ')
        preorder(left[node])
        preorder(right[node])


# --- 메인 로직 ---
V = int(input())  # 정점의 개수
E = V - 1  # 간선의 개수

# 간선 정보
# (부모, 자식) 쌍 * E개
edge = list(map(int, input().split()))

left = [0] * (V + 1)
right = [0] * (V + 1)

for i in range(E):
    parent, child = edge[2 * i], edge[2 * i + 1]

    # 왼쪽 자식이 비어있다면(첫번째 자식이라면), left에 추가
    if left[parent] == 0:
        left[parent] = child
    # 두번째 자식이라면, right에 추가
    else:
        right[parent] = child

preorder(1)
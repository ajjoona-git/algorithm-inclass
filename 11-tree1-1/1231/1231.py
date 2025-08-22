# 1231. 중위순회

# import sys
# sys.stdin = open("input.txt")


def inorder(node):
    """주어진 노드번호(node)를 루트로 하는 서브트리를 중위순회(LVR)하는 함수"""
    global result

    # node는 정점 번호
    # 리프 노드인 경우, edge[node]는 길이가 2 (예: ['5', 'T'])
    if len(edge[node]) == 2:
        result += [edge[node][1]]

    # 리프 노드가 아닌 경우, edge[node]는 ['node', 'data', 'left child', 'right child']
    # (예: ['3', 'R', '6', '7'])
    else:
        left_child = int(edge[node][2])
        inorder(left_child)
        result += [edge[node][1]]
        
        if len(edge[node]) == 4:
            right_child = int(edge[node][3])
            inorder(right_child)

        

T = 10
for tc in range(1, T+1):
    N = int(input())  # 정점의 수
    
    # 간선 정보 (input 예: 1 W 2 3)
    # edge = [[] * (N+1)]  -> [[]] 길이가 1인 빈 리스트가 생성됨
    edge = [[] for _ in range(N+1)]
    for _ in range(N):
        row = input().split()
        edge[int(row[0])] = row
    
    # 결과를 저장할 리스트
    result = []
    inorder(1)

    print(f'#{tc}', ''.join(result))

# 1232. 사칙연산

# import sys
# sys.stdin = open("input.txt")


def postorder(node):
    """주어진 노드번호(node)를 루트로 하는 서브트리를 후위순회(LRV)하면서 계산한 값을 반환하는 함수"""
    global result

    # node는 정점 번호
    # 리프 노드(피연산자)인 경우, edge[node]는 길이가 2 (예: ['4', '88'])
    # 값을 반환한다.
    if len(edge[node]) == 2:
        return float(edge[node][1])

    # 리프 노드가 아닌 경우, edge[node]는 ['node', '연산자', 'left child', 'right child']
    # (예: ['1', '/', '2', '3'])
    # 연산한 결과를 반환한다.
    else:
        left_child_num = int(edge[node][2])
        right_child_num = int(edge[node][3])
        left = postorder(left_child_num)
        right = postorder(right_child_num)

        operator = edge[node][1]
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        else:
            return left / right



T = 10
for tc in range(1, T+1):
    N = int(input())  # 정점의 수
    
    # 간선 정보 (input 예: 1 - 2 3)
    edge = [[] for _ in range(N+1)]
    for _ in range(N):
        row = input().split()
        edge[int(row[0])] = row
    
    # 연산한 결과를 정수로 출력
    # 소수점 아래는 버린다.
    result = int(postorder(1))

    print(f'#{tc} {result}')

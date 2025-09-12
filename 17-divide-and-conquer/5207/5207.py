# 5207. 이진 탐색

def binary_search(l, r, key, dir):
    """주어진 리스트 (arrA)에서 시작과 끝 인덱스를 l, r로 하여 key을 탐색한다.
        단, 탐색 과정에서 왼쪽 구간과 오른쪽 구간을 번갈아 선택하는 경우에만 count를 +1한다."""
    global count
    
    # 탐색 실패
    if l > r:
        return

    # 탐색 성공
    # (m에 찾는 원소가 있는 경우 방향을 따지지 않는다.)
    m = (l + r) // 2  # 중앙값을 기준으로
    if arrA[m] == key:
        count += 1
        return
    
    # 구간 선택
    # 조기 중단 조건: 같은 구간을 연속으로 선택한다.
    # (음수면 left, 양수면 right)
    if arrA[m] > key and dir > -1:  # left
        binary_search(l, m - 1, key, -1)
    elif arrA[m] < key and dir < 1:  # right
        binary_search(m + 1, r, key, 1)
    else:
        return



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arrA = sorted(list(map(int, input().split())))  # N개
    arrB = list(map(int, input().split()))  # M개
    
    count = 0
    for b in arrB:
        binary_search(0, N-1, b, 0)

    print(f'#{tc} {count}')

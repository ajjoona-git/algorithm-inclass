# 4839: 이진탐색

# import sys
# sys.stdin = open("sample_input.txt")

def binary_search(left, right, key, count=1):
    """
    이진 탐색을 통해 주어진 구간(연속된 정수)에서 key를 찾기까지 탐색한 횟수를 반환하는 함수

    left: 탐색할 범위의 시작 값
    right: 탐색할 범위의 끝 값
    key: 찾고 싶은 값
    count: 탐색 횟수
    """
    # 중앙 값의 인덱스
    mid = int((left + right) / 2)

    # 1. 중앙 값과 키 값이 일치
    if mid == key:
        return count

    # 2. 중앙 값보다 키 값이 크다: 오른쪽 영역을 탐색
    elif mid < key:
        return binary_search(mid, right, key, count + 1)

    # 3. 중앙 값보다 키 값이 작다: 왼쪽 영역을 탐색
    else:
        return binary_search(left, mid, key, count + 1)

    # 찾지 못한 경우
    return 0

T = int(input())

for tc in range(1, T+1):
    P, page_A, page_B = map(int, input().split())
    count_A = binary_search(1, P, page_A)
    count_B = binary_search(1, P, page_B)

    if count_A > count_B:
        winner = "B"
    elif count_A < count_B:
        winner = "A"
    else:
        winner = 0

    print(f"#{tc} {winner}")
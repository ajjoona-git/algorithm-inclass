# 1966. 숫자를 정렬하자
# 선택정렬

# import sys
# sys.stdin = open("input.txt")

def selection_sort(arr, N):
    """주어진 배열(arr)을 선택 정렬 방법으로 오름차순으로 정렬하여 반환하는 함수"""
    # i는 값을 확정할 위치의 인덱스
    for i in range(N - 1):
        # 미정렬 구간(i부터 N까지)에서 최소값을 찾아 위치를 교환한다.
        min_idx = i
        for j in range(i + 1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 배열의 크기
    arr = list(map(int, input().split()))  # 숫자 리스트

    sorted_arr = selection_sort(arr, N)

    print(f'#{tc}', end=' ')
    print(*sorted_arr)
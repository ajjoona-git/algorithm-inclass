# 1966. 숫자를 정렬하자 
# 버블정렬

# import sys
# sys.stdin = open("input.txt")

def bubble_sort(arr, N):
    """주어진 배열(arr)을 버블 정렬 방법으로 오름차순으로 정렬하여 반환하는 함수"""
    # i는 값을 확정할 위치의 인덱스 (역방향으로 순회)
    for i in range(N - 1, 0, -1):
        # 인접한 두 요소를 교환하면서 최대값의 위치를 고정해나간다.
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 배열의 크기
    arr = list(map(int, input().split()))  # 숫자 리스트

    sorted_arr = bubble_sort(arr, N)

    print(f'#{tc}', end=' ')
    print(*sorted_arr)

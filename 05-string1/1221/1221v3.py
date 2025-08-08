# 1221. GNS

# import sys
# sys.stdin = open("GNS_test_input.txt")

T = int(input())  # 테스트 케이스의 수

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

def select_sort(arr, N):
    """
    선택 정렬 방식으로 정렬한 배열을 반환하는 함수
    """
    for i in range(N-1):
        min_idx = i
        for j in range(i, N):
            if numbers.index(arr[j]) < numbers.index(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


for _ in range(T):
    # tc: 테스트 케이스의 번호(# 포함)
    # len_s: 테스트 케이스의 길이, 즉 단어의 개수
    tc, len_s = input().split()
    len_s = int(len_s)
    # s: 외계행성의 숫자들
    s = list(input().split())

    sorted_s = select_sort(s, len_s)

    print(tc)
    print(*sorted_s)
# 1221. GNS

# import sys
# sys.stdin = open("GNS_test_input.txt")

T = int(input())  # 테스트 케이스의 수

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

def bubble_sort(arr, N):
    """
    버블 정렬 방식으로 정렬한 배열을 반환하는 함수
    """
    for i in range(N-1, 0, -1):
        for j in range(i):
            if numbers.index(arr[j]) > numbers.index(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


for _ in range(T):
    # tc: 테스트 케이스의 번호(# 포함)
    # len_s: 테스트 케이스의 길이, 즉 단어의 개수
    tc, len_s = input().split()
    len_s = int(len_s)
    # s: 외계행성의 숫자들
    s = list(input().split())

    sorted_s = bubble_sort(s, len_s)

    print(tc)
    print(*sorted_s)
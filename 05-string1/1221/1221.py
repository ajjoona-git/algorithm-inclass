# 1221. GNS

# import sys
# sys.stdin = open("GNS_test_input.txt")

T = int(input())  # 테스트 케이스의 수

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

def counting_sort(arr, K):
    """
    카운팅 정렬 방식으로 정렬한 배열을 반환하는 함수
        K: 주어진 배열의 요소 중 최대값
    """
    # 카운트 배열 생성
    count = [0] * (K+1)
    for num in arr:
        count[numbers.index(num)] += 1

    # 카운트 배열 누적합
    for i in range(1, K+1):
        count[i] += count[i-1]

    # 결과 배열에 저장
    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        count[numbers.index(num)] -= 1
        sorted_arr[count[numbers.index(num)]] = num

    return sorted_arr


for _ in range(T):
    # tc: 테스트 케이스의 번호(# 포함)
    # len_s: 테스트 케이스의 길이, 즉 단어의 개수
    tc, len_s = input().split()
    len_s = int(len_s)
    # s: 외계행성의 숫자들
    s = list(input().split())

    sorted_s = counting_sort(s, 9)

    print(tc)
    print(*sorted_s)
# 4835. 구간합

# import sys
# sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N, M = map(int, input().split())  # 정수의 개수 N, 구간의 개수 M
    numbers = list(map(int, input().split()))  # 정수 리스트

    # 최소 합과 최대 합을 저장할 변수 초기화
    min_sum = M * 10000  # 정수의 최대 크기가 10000이기 때문
    max_sum = 0

    # 정수 리스트(numbers)를 순회하면서 최소 합과 최대 합을 갱신한다.
    # 탐색할 마지막 인덱스는 N - M
    for i in range(N - M + 1):
        # 구간 합을 저장할 변수 초기화
        sum_n = 0
        # 구간 합 계산
        for j in range(M):
            sum_n += numbers[i+j]
        # 최소 합 갱신
        if sum_n < min_sum:
            min_sum = sum_n
        # 최대 합 갱신
        if sum_n > max_sum:
            max_sum = sum_n

    # 최대 합과 최소 합의 차이를 출력
    print(f'#{test_case} {max_sum - min_sum}')
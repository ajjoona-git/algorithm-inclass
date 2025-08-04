import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스의 수

# 테스트 케이스의 수만큼 아래 연산을 반복한다.
for tc in range(1, T+1):
    N = int(input())  # 양수의 개수
    # N개의 양수를 입력받아 리스트 형태로 저장한다.
    arr = list(map(int, input().split()))

    # 최대값과 최소값의 인덱스를 저장할 변수
    # 첫 번째 인덱스로 초기화했다.
    max_idx = 0
    min_idx = 0

    # arr 리스트를 순회하면서
    for i in range(N):
        # 현재 인덱스의 값이 최대값보다 크면
        if arr[i] > arr[max_idx]:
            # max_idx를 갱신한다.
            max_idx = i
        # 현재 인덱스의 값이 최소값보다 작으면
        if arr[i] < arr[min_idx]:
            # min_idx를 갱신한다.
            min_idx = i

    # 가장 큰 수와 가장 작은 수의 차이를 계산한다.
    result = arr[max_idx] - arr[min_idx]

    # 결과를 출력한다.
    print(f'#{tc} {result}')
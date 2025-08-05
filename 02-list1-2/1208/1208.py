# 1208. flatten

# import sys
# sys.stdin = open("input.txt")

T = 10  # 테스트 케이스의 수

for test_case in range(1, T+1):
    dump = int(input())  # 덤프 횟수
    boxes = list(map(int, input().split()))  # 각 상자의 높이

    # 평탄화를 한다 = 최대값-1, 최소값+1
    # 상자의 총 개수는 변하지 않는다.

    # 카운팅 배열 생성
    counting_arr = [0] * (100+1)  # 상자의 높이는 1 이상 100 이하
    for box in boxes:
        counting_arr[box] += 1

    # 덤프 횟수동안 평탄화 과정을 반복한다.
    while dump >= 0:
        # 카운팅 배열을 정방향으로 순회하면서 0이 아닌 값이 나오면 최소값으로 입력
        min_value = 0
        while not counting_arr[min_value]:
            min_value += 1
        # 카운팅 배열을 역방향으로 순회하면서 0이 아닌 값이 나오면 최대값으로 입력
        max_value = 100
        while not counting_arr[max_value]:
            max_value -= 1

        # 종료 조건 1. 작업 횟수(덤프횟수)가 제한된다.
        if dump == 0:
            break

        # 종료 조건 2. 평탄화가 완료된다
        # 최대값, 최소값의 차이가 0 또는 1
        if max_value - min_value <= 1:
            break

        # 평탄화를 한다: 카운팅 배열에서 최대값과 최소값은 -1, (최대값-1)과 (최소값+1)은 +1 해준다.
        counting_arr[max_value] -= 1
        counting_arr[min_value] -= 1
        counting_arr[max_value - 1] += 1
        counting_arr[min_value + 1] += 1

        dump -= 1

    # 결과를 출력한다.
    print(f"#{test_case} {max_value - min_value}")
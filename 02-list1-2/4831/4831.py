# 4831. 전기버스

# import sys
# sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    # 한 번 충전으로 이동가능한 정류장 수 K
    # 종점 N, 충전기가 설치된 정류장 수 M
    K, N, M = map(int, input().split())

    # 충전기가 설치된 정류장 리스트
    chargers = list(map(int, input().split()))

    count = 0  # 충전횟수
    i = 0  # 현재 위치

    while i < N:
        # 현재 위치(i)에서 이동가능한 경로의 충전기를 탐색한다.
        # 역순으로 탐색함으로써 최소 충전 횟수를 구한다.
        for temp in range(i+K, i, -1):
            # 이동가능한 경로에 종점이 포함된다면 탐색을 종료한다.
            if temp >= N:
                i = N
                break
            # 충전기가 있다면 탐색 위치를 현위치로 갱신하고 충전한다.
            if temp in chargers:
                i = temp
                count += 1
                break
        # 충전기를 발견하지 못했다면 0을 반환하고 탐색을 종료한다.
        else:
            count = 0
            break

    # 결과를 출력한다.
    print(f'#{test_case} {count}')
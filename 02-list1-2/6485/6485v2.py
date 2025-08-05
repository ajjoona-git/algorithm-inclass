# 6485. 삼성시의 버스 노선

# import sys
# sys.stdin = open("s_input.txt")

T = int(input())  # 테스트 케이스의 수

# 2. Ci를 순회하면서 버스 노선에 포함되는지 계산한다.
for test_case in range(1, T+1):
    N = int(input())  # 버스 노선 개수

    routes = [0] * N  # N개의 버스노선의 출발점과 도착점 리스트
    for i in range(N):
        departure, arrival = map(int, input().split())
        routes[i] = [departure, arrival]

    P = int(input())  # 궁금한 버스 정류장의 수
    stations = [int(input()) for _ in range(P)]  # 궁금한 버스 정류장의 번호

    num_of_buses = [0] * P  # 정류장에 정차하는 버스의 수
    # 궁금한 정류장마다 각 버스 노선안에 포함되는지 확인한다.
    for i in range(P):
        for route in routes:
            # 포함되면 num_of_buses를 +1
            if route[0] <= stations[i] <= route[1]:
                num_of_buses[i] += 1

    # 결과를 출력한다.
    print(f"#{test_case}", end=" ")
    for i in range(P):
        print(num_of_buses[i], end=" ")
    print()
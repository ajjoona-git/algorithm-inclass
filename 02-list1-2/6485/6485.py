# 6485. 삼성시의 버스 노선

# import sys
# sys.stdin = open("s_input.txt")

T = int(input())  # 테스트 케이스의 수

# 1. 각 버스 정류장에 정차하는 버스의 수를 카운팅한다.
for test_case in range(1, T+1):
    N = int(input())  # 버스 노선 개수

    # 정류장에 정차하는 버스의 수.(정류장은 총 5000개)
    num_of_buses = [0] * 5001

    # routes = [0] * N  # N개의 버스노선의 출발점과 도착점 리스트
    for _ in range(N):
        departure, arrival = map(int, input().split())

        # 출발점부터 도착점까지의 stops를 +1 한다.
        for i in range(departure, arrival + 1):
            num_of_buses[i] += 1

    P = int(input())  # 궁금한 버스 정류장의 수
    stations = [int(input()) for _ in range(P)]  # 궁금한 버스 정류장의 번호

    # 결과를 출력한다.
    print(f"#{test_case}", end=" ")
    for station in stations:
        print(num_of_buses[station], end=" ")
    print()

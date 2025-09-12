# 5208. 전기버스2 

def charge(station, count):
    global min_charge
    battery = batteries[station]

    # 가지치기: 현재 카운트가 최소 카운트 이상일 때
    if count >= min_charge:
        return

    # 종료 조건: 종점 도착 가능
    if station + battery >= N:
        min_charge = min(min_charge, count)
        return
    
    # 배터리 교체
    for drive in range(battery, 0, -1):
        charge(station + drive, count + 1)


T = int(input())
for tc in range(1, T+1):
    input_list = list(map(int, input().split()))
    N = input_list[0]
    # 1 ~ N-1번 정류장의 배터리 용량
    batteries = [0] + input_list[1:]
    
    min_charge = N
    charge(1, 0)

    print(f'#{tc} {min_charge}')

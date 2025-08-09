# 연습 문제. 길 찾기 로봇

def get_final_position(commands):
    # 시작 위치
    r, c = 0, 0

    # N, S, E, W의 이동방향을 담은 델타 배열
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    directions = ['N', 'S', 'E', 'W']

    # 방향 문자열을 순회하면서 현재 위치를 이동한다.
    # 이동 중 평면을 벗어나는 입력은 없다고 가정했으므로 벽 체크는 생략한다.
    for command in commands:
        idx = directions.index(command)
        r += dr[idx]
        c += dc[idx]        

    return r, c

# 테스트
commands = ['E', 'E', 'S', 'W', 'N']
end_r, end_c = get_final_position(commands)
print(f"최종 위치: ({end_r}, {end_c})") # 최종 위치: (0, 1)
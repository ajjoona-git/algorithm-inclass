# 1206. View

# import sys
# sys.stdin = open("sample_input.txt")

T = 10  # 테스트 케이스의 수

def max_height(i):
    """입력받은 인덱스(i)를 기준으로, 인덱스 i-2, i-1, i+1, i+2의 값 중 최대값을 반환하는 함수"""
    max_h = 0
    for x in range(-2, 3):
        if x == 0:  # 입력받은 인덱스(i) 자기 자신은 제외한다.
            continue
        # 현재 값이 최대값보다 크면 최대값을 갱신한다.
        if heights[i+x] > max_h:
            max_h = heights[i+x]
    return max_h

for tc in range(1, T+1):
    N = int(input())  # 건물의 개수
    heights = list(map(int, input().split()))  # 건물의 높이

    view = 0  # 조망권이 확보된 세대 수

    # 자신을 기준으로, -2 ~ +2의 건물만 비교한다.
    for i in range(2, N-2):
        # i-2, i-1, i+1, i+2의 최대값(max_h)을 구한다.
        max_h = max_height(i)
        # 최대값이 i보다 작으면, 차이만큼 조망권을 확보할 수 있다.
        if max_h < heights[i]:
            view += (heights[i] - max_h)

    # 결과를 출력한다.
    print(f'#{tc} {view}')
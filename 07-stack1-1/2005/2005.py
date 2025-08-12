# 2005. 파스칼의 삼각형 

# import sys
# sys.stdin = open('input.txt')


def nth_pascal_triangle(N):
    """파스칼의 삼각형의 N번째 줄을 list형태로 반환하는 함수"""
    # N이 1이면 1을 반환
    if N == 1:
        return [1]
    
    # N번째 파스칼 삼각형을 저장할 리스트
    new_line = [0] * N

    # 1. N번째 파스칼 삼각형을 계산한다.
    # prior_line: N-1번째 파스칼 삼각형의 처음과 끝을 0으로 패딩 (길이는 N+1)
    prior_line = [0] + nth_pascal_triangle(N-1) + [0]
    # 각 숫자는 자신의 왼쪽과 오른쪽 위의 숫자의 합
    for i in range(N):
        new_line[i] = prior_line[i] + prior_line[i+1]
    
    return new_line


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 파스칼의 삼각형의 크기
    
    print(f'#{tc}')
    for i in range(1, N+1):
        print(*nth_pascal_triangle(i))
    
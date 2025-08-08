# 4861. 회문 

# import sys
# sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트 케이스의 수

def is_palindrome(s, M):
    """입력받은 문자열(s)이 길이가 M인 회문인지 판단하는 함수
    * 반환값: 회문이면 True , 회문이 아니라면 False"""

    # 회문의 절반 길이만큼 순회하면서 현재 문자와 뒤에서부터 인덱싱한 문자를 비교한다.
    for i in range(M//2):
        if s[i] != s[-1-i]:  # 값이 다르면 False
            return False

    return True  # 무사히 검사를 마쳤다면 True

for tc in range(1, T+1):
    N, M = map(int, input().split())  # 글자판의 크기 N, 회문의 길이 M
    letters_hor = [input() for _ in range(N)]  # 글자판 원본
    letters_ver = list(map(list, zip(*letters_hor)))  # 세로 방향 탐색을 위한 전치 행렬

    # 회문을 담을 빈 문자열 (letters_ver을 위해 초기화함)
    result = ''

    for r in range(N):
        for c in range(N-M+1):
            # 가로 방향 탐색
            if is_palindrome(letters_hor[r][c:c+M], M):
                result = letters_hor[r][c:c+M]
            # 세로 방향 탐색
            elif is_palindrome(letters_ver[r][c:c+M], M):
                # letters_ver 은 2차원 리스트 형태이기 때문에 문자열로 형변환이 필요하다
                for s in letters_ver[r][c:c+M]:
                    result += s


    print(f'#{tc} {result}')
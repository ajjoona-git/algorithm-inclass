# 1989. 초심자의 회문 검사

# import sys
# sys.stdin = open("input.txt")

T = int(input())  # 테스트 케이스의 수

def is_palindrome(s):
    """입력받은 문자열(s)이 회문인지 판단하는 함수
       * 반환값: 회문이면 1, 회문이 아니라면 0"""
    # 문자열의 절반 길이만큼 순회하면서 현재 문자와 뒤에서부터 인덱싱한 문자를 비교한다.
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:  # 값이 다르면 False
            return 0
    return 1  # 무사히 검사를 마쳤다면 True

for tc in range(1, T+1):
    s = input()
    print(f'#{tc} {is_palindrome(s)}')
# 1216. 회문2
# 시간이 너무 많이 걸림! (테스트케이스는 나오는데, 제출하면 output 안 나옴)

import sys
sys.stdin = open('input.txt')

def is_palindrome(word, k):
    for i in range(k//2):
        if word[i] != word[-1-i]:
            return False
    else:
        return True


T = 10
for _ in range(T):
    tc = input().strip()  # 테스트 케이스의 번호
    N = 100  # 배열의 크기
    arr = [input() for _ in range(N)]

    max_len = 0  # 회문의 최대 길이

    # 현재 위치(i, j)를 이동한다. 
    for i in range(N):
        for j in range(N):
            # k: 탐색할 단어의 길이 (N-j 부터 max_len 까지. 최대 길이부터 탐색)
            for k in range(N-j, max_len, -1):
                # 가로 문자
                # 최대 길이 갱신
                if is_palindrome(arr[i][j:j+k], k) and k > max_len:
                    max_len = k
            
                # 세로 문자
                word = list(zip(*arr[j:j+k]))[i]
                if is_palindrome(word, k) and k > max_len:
                    max_len = k
            
    
    print(f'#{tc} {max_len}')
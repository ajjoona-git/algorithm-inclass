# 1216. 회문2

# import sys
# sys.stdin = open('input.txt')

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
    rotated_arr = list(zip(*arr))  # 전치 행렬

    max_len = 0  # 회문의 최대 길이

    # 현재 위치를 이동하면서 가로, 세로 회문의 개수를 더한다.
    for i in range(N):
        for j in range(N):
            # k: 탐색할 단어의 길이 (N-j 부터 max_len 까지. 최대 길이부터 탐색)
            for k in range(N-j, max_len, -1):
                # 현재 탐색할 단어의 길이(k)가 최대 길이보다 짧으면 다음 위치로 넘어간다.
                # if k <= max_len:
                #     break
                # 최대 길이 갱신
                if is_palindrome(arr[i][j:j+k], k):
                    max_len = k
                if is_palindrome(rotated_arr[i][j:j+k], k):
                    max_len = k
    
    print(f'#{tc} {max_len}')
# 1215. 회문1

# import sys
# sys.stdin = open('input.txt')

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

T = 10
for tc in range(1, T+1):
    K = int(input())  # 회문의 길이
    N = 8  # 배열의 크기
    arr = [input() for _ in range(N)]
    rotated_arr = list(zip(*arr))  # 전치 행렬

    count = 0  # 회문의 개수

    # 현재 위치를 이동하면서 가로, 세로 회문의 개수를 더한다.
    for i in range(N):
        for j in range(N - K + 1):
            if is_palindrome(arr[i][j:j+K]):
                count += 1
            if is_palindrome(rotated_arr[i][j:j+K]):
                count += 1
    
    print(f'#{tc} {count}')
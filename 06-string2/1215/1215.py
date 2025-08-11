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

    count = 0  # 회문의 개수

    for i in range(N):
        for j in range(N):
            # 가로 체크
            if j+K <= N and is_palindrome(arr[i][j:j+K]):
                count += 1
            
            # 세로 체크
            word = list(zip(*arr[i:i+K]))[j]
            if i+K <= N and is_palindrome(word):
                count += 1

    
    print(f'#{tc} {count}')
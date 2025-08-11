# 4864. 문자열 비교

# import sys
# sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # 문자열의 길이
    n = len(str1)
    m = len(str2)

    # 결과 (존재하면 1, 존재하지 않으면 0)
    result = 0

    # str2를 순회하면서 str1과 같은지 비교
    for i in range(m - n + 1):
        if str2[i : i + n] == str1:
            result = 1
            break
    
    print(f'#{tc} {result}')
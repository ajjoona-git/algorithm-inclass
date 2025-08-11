# 10804. 문자열의 거울상

# import sys
# sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    original_str = input()  # 원본 문자열
    reflection = ''  # 거울에 비친 문자열

    # 문자열을 뒤에서부터 순회하면서 b <-> d, p <-> q 바꾸기
    for i in range(len(original_str)-1, -1, -1):
        if original_str[i] == 'b':
            reflection += 'd'
        elif original_str[i] == 'd':
            reflection += 'b'
        elif original_str[i] == 'p':
            reflection += 'q'
        else:
            reflection +='p'

    print(f'#{tc} {reflection}')
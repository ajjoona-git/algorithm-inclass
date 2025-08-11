# 3143. 가장 빠른 문자열 타이핑

import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    full_str, key_str = input().split()
    
    # 전체 문자열에서 패턴을 찾아서 한 글자('-')로 바꾼다.
    min_str = full_str.replace(key_str, '-')

    print(f'#{tc} {len(min_str)}')

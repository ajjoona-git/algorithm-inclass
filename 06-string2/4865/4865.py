# 4865. 글자수

# import sys
# sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # str1의 문자들과 출현 횟수를 딕셔너리로 저장한다.
    # 이때 key가 중복되지 않기 위해 setdefault 메서드를 활용한다.
    str_count = {}
    for char in str1:
        str_count.setdefault(char, 0)

    # str2의 문자들을 순회하면서 str1에 포함된 글자라면, 카운트 값을 +1
    for char in str2:
        if char in str_count.keys():
            str_count[char] += 1
    
    # 가장 많은 글자의 수
    max_count = max(str_count.values())

    print(f'#{tc} {max_count}')

    
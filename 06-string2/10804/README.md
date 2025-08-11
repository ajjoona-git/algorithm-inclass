# 10804. 문자열의 거울상 | D3

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXTC0x16D8EDFASe&categoryId=AXTC0x16D8EDFASe&categoryType=CODE&problemTitle=%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%98+%EA%B1%B0%EC%9A%B8%EC%83%81&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **문자열 처리**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받습니다.
2.  각 테스트 케이스마다 원본 문자열 `original_str`을 입력받습니다.
3.  거울에 비친 문자열을 저장할 `reflection` 변수를 빈 문자열로 초기화합니다.
4.  원본 문자열을 뒤에서부터 순회하는 `for` 반복문을 사용합니다. `range(len(original_str)-1, -1, -1)`를 통해 문자열의 마지막 문자부터 첫 번째 문자까지 역순으로 순회합니다.
5.  각 문자에 대해 조건문을 사용하여 거울상이 되는 문자로 치환합니다.
    * `'b'`는 `'d'`로
    * `'d'`는 `'b'`로
    * `'p'`는 `'q'`로
    * `'q'`는 `'p'`로
6.  치환된 문자를 `reflection` 문자열에 이어붙입니다.
7.  모든 순회가 끝나면 `reflection`에 저장된 거울상 문자열을 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [10804.py](10804.py)
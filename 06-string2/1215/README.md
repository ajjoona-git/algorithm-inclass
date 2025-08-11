# 1215. 회문1 | D3

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE&problemTitle=1215&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식 1

### 1. 사용 알고리즘
* **구현(Implementation)**
* **회문 검사**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 회문 여부를 확인할 문자열 `s`를 입력받습니다.
2.  `is_palindrome(s)`라는 함수를 정의하여 회문 여부를 판별합니다.
3.  함수 내부에서는 `for` 반복문을 사용하여 문자열의 절반 길이(`len(s)//2`)만큼 순회합니다.
4.  각 `i`번째 인덱스의 문자(`s[i]`)와 뒤에서부터 `i`번째에 해당하는 문자(`s[-1-i]`)를 비교합니다.
5.  두 문자가 다르면 회문이 아니므로 즉시 `0`을 반환하며 함수를 종료합니다.
6.  `for` 반복문이 끝까지 문제없이 실행되면, 문자열은 회문이므로 `1`을 반환합니다.
7.  각 테스트 케이스마다 `is_palindrome` 함수를 호출하여 결과를 얻고, 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [1215.py](1215.py)


## 💡 접근 방식 2

### 1. 사용 알고리즘
* **구현(Implementation)**
* **2차원 배열 순회** 및 **회문 검사**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 회문의 길이 `K`와 8x8 크기의 글자판 `arr`를 입력받습니다.
2.  `zip(*arr)`를 활용하여 행과 열을 바꾼 **전치 행렬** `rotated_arr`를 생성합니다. 이를 통해 세로 방향의 회문을 가로 방향 탐색과 동일한 방식으로 검사할 수 있습니다.
3.  `is_palindrome(word)` 함수를 정의하여, 입력받은 문자열이 회문인지 여부를 `word == word[::-1]`과 같이 간결하게 판별합니다.
4.  이중 반복문을 사용하여 `arr`의 모든 행(`i`)과 열(`j`)을 순회하며, 길이가 `K`인 부분 문자열을 슬라이싱하여 회문인지 확인합니다.
5.  **가로 방향** 회문은 `arr[i][j:j+K]`로, **세로 방향** 회문은 `rotated_arr[i][j:j+K]`로 검사합니다.
6.  `is_palindrome` 함수를 호출하여 회문이 발견되면 `count` 변수를 1 증가시킵니다.
7.  모든 탐색이 끝나면 `count`에 저장된 최종 회문의 개수를 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [1215v2.py](1215v2.py)
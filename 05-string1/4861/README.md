# 4861. 회문 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AWTQQXcKQHkDFAVT&probBoxId=AZh-M3iq4UjHBINp&type=PROBLEM&problemBoxTitle=String&problemBoxCnt=5)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **2차원 배열 순회** 및 **문자열 슬라이싱**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 글자판의 크기 `N`과 회문의 길이 `M`을 입력받습니다.
2.  `N x N` 크기의 글자판 `letters_hor`를 2차원 리스트로 저장합니다.
3.  세로 방향으로 탐색하기 위해 `zip(*letters_hor)`를 활용하여 행과 열을 바꾼 새로운 글자판 `letters_ver`를 생성합니다.
4.  주어진 문자열이 회문인지 판별하는 함수 `is_palindrome`을 정의합니다. 이 함수는 문자열의 절반 길이만큼 순회하며 앞뒤 문자를 비교하여 회문 여부를 판별합니다.
5.  `letters_hor`와 `letters_ver`를 순회하면서 길이가 `M`인 모든 부분 문자열을 슬라이싱하여 회문인지 확인합니다.
6.  회문을 발견하면 `result` 변수에 해당 문자열을 저장합니다.
7.  모든 탐색이 끝난 후, `result`에 저장된 회문 문자열을 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [4861.py](4861.py)
# 1989. 초심자의 회문 검사 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AV5PyTLqAf4DFAUq&probBoxId=AZh-M3iq4UjHBINp&type=PROBLEM&problemBoxTitle=String&problemBoxCnt=5&&&&&&)

## 💡 접근 방식

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
* [1989.py](1989.py)
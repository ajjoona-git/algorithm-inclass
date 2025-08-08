# 4839: 이진탐색 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AWTLcyA6qAMDFAVT&probBoxId=AZh9Pr4Kw1rHBINp&type=PROBLEM&problemBoxTitle=List&problemBoxCnt=21)

## 💡 접근 방식

### 1. 사용 알고리즘
* **이진 탐색(Binary Search)**
* **재귀(Recursion)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 `P`(총 페이지), `page_A`, `page_B`를 입력받습니다.
2.  이진 탐색 과정을 **재귀 함수 `binary_search(left, right, key, count)`**로 구현합니다. 이 함수는 탐색 범위의 시작(`left`), 끝(`right`), 찾고자 하는 페이지(`key`), 그리고 탐색 횟수(`count`)를 인자로 받습니다.
3.  함수 내부에서는 탐색 범위의 중간 값 `mid`를 계산합니다.
4.  `mid`가 `key`와 일치하면 현재까지의 탐색 횟수 `count`를 반환하며 재귀 호출을 종료합니다.
5.  `mid`가 `key`보다 작다면 `mid`부터 `right`까지의 오른쪽 절반을 탐색하도록 함수를 재귀 호출하고, `count`를 1 증가시킵니다.
6.  `mid`가 `key`보다 크다면 `left`부터 `mid`까지의 왼쪽 절반을 탐색하도록 재귀 호출합니다.
7.  각 테스트 케이스마다 `binary_search` 함수를 `page_A`와 `page_B`에 대해 각각 호출하여 탐색 횟수 `count_A`와 `count_B`를 얻습니다.
8.  두 사람의 탐색 횟수를 비교하여 횟수가 더 적은 쪽이 승자가 되며, 횟수가 같으면 `0`을 출력하도록 결과를 판별합니다.
9.  최종 결과를 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [4839.py](4839.py)
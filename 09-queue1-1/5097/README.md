# 5097. 회전 | D2

## 문제 출처
![SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AWTVjgHKbn8DFAVT&probBoxId=AZh9VAAaxs3HBINp&type=PROBLEM&problemBoxTitle=Queue&problemBoxCnt=6)

## 💡 접근 방식


### 1. 사용 알고리즘
* **구현(Implementation)**
* **큐(Queue)** 자료구조 (`collections.deque` 모듈 활용)

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 수열의 길이 `N`과 회전 횟수 `M`을 입력받습니다.
2.  입력받은 수열 `arr`을 `collections.deque` 자료형으로 변환합니다. `deque`는 양 끝에서 효율적으로 요소를 추가하거나 제거할 수 있어, 회전 연산에 최적화되어 있습니다.
3.  `deque`의 `rotate()` 메소드를 사용하여 수열을 `M`번 회전시킵니다. `rotate(-M)`은 왼쪽으로 `M`번 회전하는 것과 동일합니다.
4.  `M`번의 회전이 끝난 후, `arr_deque[0]`을 통해 가장 앞에 있는 요소를 찾습니다.
5.  최종 결과를 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [5097.py](5097.py)
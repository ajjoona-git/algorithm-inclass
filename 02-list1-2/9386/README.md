# 9386. 연속한 1의 개수 | D1

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXALDUIq97oDFASI&categoryId=AXALDUIq97oDFASI&categoryType=CODE/)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **반복문**과 **상태 관리**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 수열의 길이 `N`과 0과 1로 구성된 수열 `binary`를 입력받습니다.
2.  연속된 1의 개수를 셀 `count`와 그 중 최대값을 저장할 `max_count` 변수를 `0`으로 초기화합니다.
3.  수열 `binary`를 순회하면서 각 문자가 `1`인지 `0`인지 확인합니다.
4.  만약 현재 문자가 `1`이면 `count`를 1 증가시켜 연속된 1의 개수를 카운트합니다.
5.  현재 문자가 `0`이면, 연속된 1의 개수가 끊겼다는 뜻이므로 `count`가 `max_count`보다 큰지 확인하여 `max_count`를 갱신하고, `count`를 `0`으로 초기화합니다.
6.  `for` 반복문이 끝난 후, 수열의 마지막이 연속된 1로 끝나는 경우를 처리하기 위해 `count`와 `max_count`를 다시 한 번 비교하여 `max_count`를 최종 갱신합니다.
7.  최종적으로 `max_count`에 저장된 값을 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [9386.py](9386.py)
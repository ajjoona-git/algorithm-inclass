# 12712: 파리퇴치3 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AXuARWAqDkQDFARa&probBoxId=AZh9Pr4Kw1rHBINp&type=USER&problemBoxTitle=List&problemBoxCnt=54)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **2차원 배열 순회** 및 **방향 벡터(Delta Array)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 배열의 크기 `N`과 스프레이의 세기 `M`을 입력받습니다.
2.  `N x N` 크기의 `flies` 배열을 입력받아 저장합니다.
3.  `+` 모양 스프레이와 `x` 모양 스프레이에 대한 파리 잡는 로직을 각각 `kill_flies_plus`, `kill_flies_x` 함수로 분리하여 구현합니다.
    * 두 함수 모두 현재 위치 `(r, c)`와 스프레이 세기 `M`을 인자로 받습니다.
    * 델타 배열을 사용하여 `+` 모양(상하좌우)과 `x` 모양(대각선)으로 탐색 방향을 정의합니다.
    * `for step in range(1, M)` 반복문을 통해 스프레이의 세기만큼 퍼져나가는 범위를 계산합니다.
    * 탐색 범위 내에 있는 파리의 개수를 합산하여 반환합니다.
4.  이중 반복문을 사용해 `flies` 배열의 모든 위치 `(r, c)`를 순회하면서 각 위치에 대해 `kill_flies_plus` 함수와 `kill_flies_x` 함수를 호출하여 파리 수를 계산합니다.
5.  계산된 두 값과 현재까지의 최대 파리 수(`max_flies`)를 비교하여 `max_flies`를 갱신합니다.
6.  모든 위치에 대한 계산이 끝나면, `max_flies`에 저장된 최종 값을 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [12712.py](12712.py)
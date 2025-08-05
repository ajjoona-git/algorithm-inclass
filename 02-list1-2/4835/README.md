# 4835. 구간합 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTLXCuapdcDFAVT&categoryId=AWTLXCuapdcDFAVT&categoryType=CODE)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **슬라이딩 윈도우(Sliding Window)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 정수의 개수 `N`, 구간의 개수 `M`을 입력받습니다.
2.  `N`개의 정수를 담은 리스트 `numbers`를 입력받습니다.
3.  최소 합과 최대 합을 저장할 `min_sum`, `max_sum` 변수를 초기화합니다. `min_sum`은 초기값을 충분히 큰 값으로 설정하고, `max_sum`은 0으로 초기화합니다.
4.  `numbers` 리스트를 순회하며 **슬라이딩 윈도우** 기법을 사용하여 길이가 `M`인 모든 구간의 합을 계산합니다.
5.  `for i in range(N - M + 1)` 반복문을 통해 윈도우의 시작 인덱스를 `0`부터 `N-M`까지 이동시킵니다.
6.  각 윈도우 구간(`i`부터 `i+M-1`까지)의 합 `sum_n`을 계산합니다.
7.  `sum_n`이 현재 `min_sum`보다 작으면 `min_sum`을 갱신하고, `max_sum`보다 크면 `max_sum`을 갱신합니다.
8.  모든 구간의 합을 계산한 후, `max_sum`과 `min_sum`의 차이를 계산하여 `result`에 저장합니다.
9.  최종 결과를 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.

---

### 💻 코드
* [4835.py](4835.py)
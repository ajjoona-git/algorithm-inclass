# 6485. 삼성시의 버스 노선 | D3

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWczm7QaACgDFAWn&categoryId=AWczm7QaACgDFAWn&categoryType=CODE&problemTitle=6485&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식 1

### 1. 사용 알고리즘
* **구현(Implementation)**
* **배열(Array)**을 활용한 빈도수 계산

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 버스 노선의 개수 `N`을 입력받습니다.
2.  총 5000개의 정류장에 대한 버스 정차 횟수를 기록할 `num_of_buses` 배열을 5001 크기로 0으로 초기화하여 생성합니다.
3.  `N`개의 버스 노선 정보를 입력받아, 각 노선의 출발점부터 도착점까지의 모든 정류장에 대해 `num_of_buses` 배열의 해당 인덱스 값을 1씩 증가시킵니다.
4.  궁금한 버스 정류장의 수 `P`와 그 정류장 번호가 담긴 리스트 `stations`를 입력받습니다.
5.  `stations` 리스트를 순회하면서, 각 정류장 번호에 해당하는 `num_of_buses` 배열의 값을 찾아 출력합니다.

---

### 💻 코드
* [6485.py](6485.py)


### 💡 접근 방식 2

### 1. 사용 알고리즘
* **구현(Implementation)**
* **배열(Array)**을 활용한 빈도수 계산

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 버스 노선의 개수 `N`을 입력받습니다.
2.  총 5000개의 정류장에 대한 버스 정차 횟수를 기록할 `num_of_buses` 배열을 5001 크기로 0으로 초기화하여 생성합니다.
3.  `N`개의 버스 노선 정보를 입력받아, 각 노선의 출발점부터 도착점까지의 모든 정류장에 대해 `num_of_buses` 배열의 해당 인덱스 값을 1씩 증가시킵니다.
4.  궁금한 버스 정류장의 수 `P`와 그 정류장 번호가 담긴 리스트 `stations`를 입력받습니다.
5.  `stations` 리스트를 순회하면서, 각 정류장 번호에 해당하는 `num_of_buses` 배열의 값을 찾아 출력합니다.

---

### 💻 코드
* [6485v2.py](6485v2.py)
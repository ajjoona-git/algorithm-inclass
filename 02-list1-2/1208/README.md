# 1208. Flatten | D3

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=1208&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **카운팅 정렬(Counting Sort)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`가 10으로 고정되어 있으며, 각 테스트 케이스마다 덤프 횟수 `dump`와 상자의 높이를 담은 리스트 `boxes`를 입력받습니다.
2.  `boxes` 리스트의 높이 범위(1~100)를 고려하여 길이가 101인 `counting_arr`를 생성합니다. `counting_arr`의 인덱스는 상자의 높이를, 값은 해당 높이를 가진 상자의 개수를 의미합니다.
3.  `boxes`를 순회하며 `counting_arr`에 각 높이의 상자 개수를 기록합니다.
4.  `while` 반복문을 사용하여 `dump` 횟수만큼 평탄화 과정을 반복합니다.
5.  매 반복마다 `counting_arr`를 순회하여 가장 낮은 높이(`min_value`)와 가장 높은 높이(`max_value`)를 찾습니다.
    * `min_value`는 `counting_arr`를 정방향으로 순회하며 값이 `0`이 아닌 첫 번째 인덱스를 찾아 갱신합니다.
    * `max_value`는 `counting_arr`를 역방향으로 순회하며 값이 `0`이 아닌 첫 번째 인덱스를 찾아 갱신합니다.
6.  평탄화가 완료되는 두 가지 조건을 확인하여 반복문을 종료합니다.
    * `dump` 횟수가 0이 되면 반복을 멈춥니다.
    * `max_value - min_value`가 `1` 이하면 평탄화가 완료된 것으로 간주하고 반복을 멈춥니다.
7.  평탄화 과정은 다음과 같이 `counting_arr`를 직접 수정하여 구현합니다.
    * `counting_arr[max_value]`와 `counting_arr[min_value]`를 1씩 감소시킵니다.
    * `counting_arr[max_value - 1]`과 `counting_arr[min_value + 1]`을 1씩 증가시킵니다.
8.  덤프 횟수를 1 감소시킵니다.
9.  반복문이 종료되면 `max_value - min_value`를 계산하여 결과를 출력합니다.


---

## 💻 코드
* [1208.py](1208.py)
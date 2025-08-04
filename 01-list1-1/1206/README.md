# 1206. View

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=1206&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **배열 순회(Array Traversal)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`가 10으로 고정되어 있으며, 각 테스트 케이스마다 건물의 개수 `N`과 건물의 높이를 담은 리스트 `heights`를 입력받습니다.
2.  조망권이 확보된 세대 수를 저장할 변수 `view`를 `0`으로 초기화합니다.
3.  건물 리스트를 순회하며 조망권이 확보된 건물을 찾습니다. 이때, 양쪽 끝 2개의 건물은 항상 조망권을 확보할 수 없으므로, 인덱스 `2`부터 `N-2`까지의 건물만 탐색합니다.
4.  각 건물(`i`)에 대해, 해당 건물을 기준으로 양옆 2칸씩(총 4개의 건물)의 높이를 확인합니다. 이 4개의 건물 높이 중 최댓값을 구하는 함수 `max_height`를 활용합니다.
5.  만약 현재 건물의 높이(`heights[i]`)가 주변 4개의 건물 중 가장 높은 건물(`max_h`)의 높이보다 높다면, 해당 건물은 조망권을 확보한 것으로 판단합니다.
6.  조망권이 확보된 경우, 현재 건물의 높이에서 주변 건물 중 가장 높은 건물의 높이를 뺀 값(`heights[i] - max_h`)을 `view` 변수에 더합니다.
7.  모든 건물을 탐색한 후, 최종적으로 `view`에 저장된 조망권 세대 수를 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.

---

### 💻 코드
* [1206.py](1206.py)
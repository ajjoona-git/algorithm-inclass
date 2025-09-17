# 1251. 하나로 | D4

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD&categoryId=AV15StKqAQkCFAYD&categoryType=CODE&problemTitle=1251&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&)


## 💡 접근 방식

### 1. 사용 알고리즘
* **최소 신장 트리 (Minimum Spanning Tree, MST)**
* **프림 알고리즘 (Prim's Algorithm)**
* **그리디 알고리즘 (Greedy Algorithm)**
* **우선순위 큐 (Priority Queue) / 힙 (Heap)**

### 2. 문제 풀이 과정
1.  **문제 모델링**: N개의 모든 섬을 최소 비용으로 연결하는 문제입니다. 이는 각 섬을 정점(Vertex)으로, 두 섬을 잇는 해저터널 건설 비용을 간선(Edge)의 가중치로 하는 **완전 그래프(Complete Graph)**에서 **최소 신장 트리(MST)**를 찾는 것과 같습니다.
2.  **간선 가중치 계산**: 두 섬 사이의 해저터널 건설 비용(가중치)은 `E * L^2` (환경 부담 세율 × 거리의 제곱)로 계산됩니다.
3.  **알고리즘 선택**: MST를 찾는 대표적인 알고리즘 중 하나인 **프림(Prim) 알고리즘**을 사용합니다. 프림 알고리즘은 임의의 한 정점에서 시작하여, 현재까지 만들어진 트리에 인접한 간선 중 가장 가중치가 낮은 간선을 선택하여 트리를 확장해 나가는 **그리디(Greedy)** 방식입니다.
4.  **우선순위 큐를 이용한 구현**:
    * **`dist` 배열**: 아직 MST에 포함되지 않은 각 섬(`i`)을 현재까지 만들어진 MST와 연결하는 데 필요한 최소 비용을 `dist[i]`에 저장합니다.
    * **`visited` 배열**: 각 섬이 MST에 포함되었는지 여부를 확인합니다.
    * **우선순위 큐 (최소 힙)**: `dist` 배열의 값 중 가장 작은 값을 가진 섬을 효율적으로 찾기 위해 사용합니다. 큐에는 `(비용, 섬 번호)` 튜플을 저장하여 항상 최소 비용의 간선을 먼저 처리하도록 합니다.
5.  **프림 알고리즘 탐색 과정**:
    1.  임의의 시작 섬(0번)의 `dist` 값을 0으로 설정하고 우선순위 큐에 `(비용:0, 섬:0)`을 넣고 탐색을 시작합니다.
    2.  큐가 빌 때까지 다음을 반복합니다.
    3.  큐에서 현재 가장 비용이 낮은 `(curr_cost, curr_node)`를 꺼냅니다.
    4.  만약 `curr_node`가 이미 방문한 섬이라면 무시하고 넘어갑니다.
    5.  `curr_node`를 MST에 포함시키고, `min_cost`에 `curr_cost`를 더합니다.
    6.  새롭게 MST에 포함된 `curr_node`를 기준으로, 아직 MST에 포함되지 않은 다른 모든 섬(`next_node`)까지의 터널 건설 비용을 계산합니다.
    7.  만약 계산된 비용이 `dist[next_node]`에 저장된 기존 비용보다 작다면, `dist` 값을 갱신하고 `(갱신된 비용, next_node)`를 우선순위 큐에 추가합니다.
6.  **결과 도출**: 모든 섬이 MST에 포함되면 탐색이 종료되고, `min_cost`에 저장된 값이 MST의 최종 비용이 됩니다.

---

## 💻 코드
* [1251.py](1251.py)


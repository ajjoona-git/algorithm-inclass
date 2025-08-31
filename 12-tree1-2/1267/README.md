# 1267. 작업 순서 | D6

## 문제 출처
![SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN&categoryId=AV18TrIqIwUCFAZN&categoryType=CODE&problemTitle=1267&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)


## 💡 접근 방식

### 1. 사용 알고리즘
* **그래프 (Graph) / 방향 비순환 그래프 (DAG)**
* **위상 정렬 (Topological Sort)**
* **깊이 우선 탐색 (DFS, Depth-First Search)**

### 2. 문제 풀이 과정
1.  **문제 모델링**: 주어진 작업 순서는 선행 작업이 끝나야 다음 작업을 수행할 수 있는 의존성을 가집니다. 이는 정점(Vertex)이 작업이 되고, 간선(Edge)이 작업의 선후 관계를 나타내는 **방향 비순환 그래프(DAG, Directed Acyclic Graph)**로 모델링할 수 있습니다. 문제의 목표는 이 그래프를 **위상 정렬(Topological Sort)**하는 것입니다.
2.  **DFS를 이용한 위상 정렬**: 깊이 우선 탐색(DFS)을 응용하여 위상 정렬을 구현할 수 있습니다. 핵심 아이디어는 **어떤 작업을 완료 목록에 추가하기 전에, 그 작업에 의존하는 모든 후행 작업들이 먼저 완료 목록에 추가되어야 한다는 것**입니다.
3.  **재귀 DFS 함수 설계**:
    * `dfs(curr_node)` 함수는 현재 작업(`curr_node`)을 기준으로 탐색을 시작합니다.
    * `visited` 배열을 통해 이미 처리된 노드는 다시 방문하지 않도록 합니다.
    * 현재 노드에서 출발하는 모든 후행 작업(`next_node`)에 대해, 아직 방문하지 않았다면 `dfs(next_node)`를 재귀적으로 호출합니다.
    * **핵심 로직**: `curr_node`의 모든 후행 작업에 대한 재귀 호출이 끝난 후 (즉, `curr_node`를 선행 조건으로 하는 모든 작업들이 `result`에 추가된 후), `curr_node`를 `result` 리스트의 **맨 앞에 추가(`insert(0, ...)`)**합니다.
    * 이렇게 하면, 나중에 탐색이 끝난 노드(선행 작업)가 항상 먼저 탐색이 끝난 노드(후행 작업)보다 앞에 위치하게 되어 올바른 작업 순서가 만들어집니다.
4.  **전체 그래프 탐색**:
    * `for` 루프를 통해 1번부터 V번까지의 모든 노드를 확인합니다.
    * 아직 방문하지 않은 노드가 있다면, 해당 노드를 시작점으로 `dfs`를 호출합니다. 이는 선행 작업이 없는 여러 개의 시작점이 존재하거나, 그래프가 여러 컴포넌트로 나뉘어 있는 경우에도 모든 작업을 처리하기 위함입니다.
5.  **결과 출력**: 모든 노드에 대한 탐색이 끝나면 `result` 리스트에는 위상 정렬된 작업 순서가 저장되며, 이를 형식에 맞게 출력합니다.

---

## 💻 코드
* [1267.py](1267.py)
# 7465. 창용 마을 무리의 개수 | D4

## 문제 출처
![SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU&categoryId=AWngfZVa9XwDFAQU&categoryType=CODE&problemTitle=%EC%B0%BD%EC%9A%A9&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)


## 💡 접근 방식

### 1. 사용 알고리즘
* **그래프 (Graph)**
* **깊이 우선 탐색 (DFS, Depth-First Search)**
* **연결 요소 (Connected Components)**

### 2. 문제 풀이 과정
1.  **그래프 모델링**: 마을 사람들을 정점(Vertex)으로, 서로 아는 관계를 간선(Edge)으로 하는 **무방향 그래프**로 간주합니다. '무리의 개수'는 그래프의 **연결 요소(Connected Component)의 개수**를 찾는 것과 같습니다.
2.  **인접 리스트**: 그래프의 연결 관계를 표현하기 위해 **인접 리스트(`adj_list`)**를 사용합니다. `adj_list[i]`는 `i`번 사람과 직접적으로 아는 모든 사람의 번호를 리스트로 저장합니다.
3.  **무리의 개수 세기**:
    * 모든 사람이 어떤 무리에 속해있는지 확인하기 위해 `visited` 배열을 사용합니다.
    * 1번 사람부터 N번 사람까지 순회하면서, 아직 방문하지 않은(`not visited[i]`) 사람을 찾습니다.
    * 아직 방문하지 않은 사람 `i`를 발견했다는 것은, 이 사람이 속한 무리가 아직 탐색되지 않은 **새로운 무리**라는 의미입니다.
4.  **DFS를 이용한 무리 탐색**:
    * 새로운 무리를 발견하면, `group_count`를 1 증가시킵니다.
    * 발견한 사람 `i`를 시작점으로 `dfs(i)`를 호출합니다.
    * `dfs` 함수는 스택을 이용하여 `i`와 직간접적으로 연결된 모든 사람(같은 무리에 속한 모든 구성원)을 찾아 `visited` 배열에 방문 표시를 합니다.
    * `dfs`가 종료되면, `i`가 속한 무리 전체가 방문 처리됩니다.
5.  **결과 도출**: 1번부터 N번까지의 모든 사람에 대한 확인이 끝나면, `group_count`에 최종적으로 계산된 무리의 총개수가 저장됩니다. `dfs`를 통해 한 번 발견된 무리의 모든 구성원은 방문 처리되므로, 같은 무리가 중복으로 계산되는 것을 효과적으로 방지할 수 있습니다.



---

## 💻 코드
* [7465.py](7465.py)
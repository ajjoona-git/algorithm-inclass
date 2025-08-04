# 4828. min max

## 문제 출처
[SWEA](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)
## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **배열 순회(Array Traversal)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스를 순회합니다.
2.  각 테스트 케이스마다 양수의 개수 `N`과 `N`개의 양수를 담은 리스트 `arr`를 입력받습니다.
3.  리스트에서 최댓값과 최솟값을 찾기 위해, 초기 `max_idx`와 `min_idx`를 `0`으로 설정합니다.
4.  `arr` 리스트를 순회하며 각 요소 `arr[i]`의 값을 `arr[max_idx]` 및 `arr[min_idx]`와 비교합니다.
5.  만약 `arr[i]`가 현재까지의 최댓값(`arr[max_idx]`)보다 크다면 `max_idx`를 `i`로 갱신합니다.
6.  마찬가지로 `arr[i]`가 현재까지의 최솟값(`arr[min_idx]`)보다 작다면 `min_idx`를 `i`로 갱신합니다.
7.  모든 요소를 순회한 후, `arr[max_idx]`에는 리스트의 최댓값이, `arr[min_idx]`에는 리스트의 최솟값이 저장됩니다.
8.  두 값의 차이인 `arr[max_idx] - arr[min_idx]`를 계산하여 `result`에 저장합니다.
9.  최종 결과를 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.

---

### 💻 코드
* [4828.py](4828.py)
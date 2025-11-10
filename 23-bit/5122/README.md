# 5122. 수열 편집

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTVuc46cSIDFAVT)

## 💡 접근 방식

### 1. 사용 알고리즘
* **자료 구조 (단일 연결 리스트)**: 문제에서 요구하는 특정 인덱스에서의 삽입, 삭제, 변경 연산을 처리하기 위해 **단일 연결 리스트(Singly Linked List)**를 직접 구현하여 사용합니다.

### 2. 문제 풀이 과정
1.  데이터와 다음 노드를 가리키는 포인터를 갖는 `Node` 클래스를 정의합니다.
2.  `Node`들을 관리하는 `SinglyLinkedList` 클래스를 정의하고, 문제 요구사항에 맞는 다음 메서드들을 구현합니다.
    * `append(data)`: 리스트의 맨 마지막에 노드를 추가합니다.
    * `insert(data, position)`: `position` 인덱스에 `data`를 가진 새 노드를 삽입합니다.
    * `delete(position)`: `position` 인덱스의 노드를 삭제합니다.
    * `update(data, position)`: `position` 인덱스의 노드 값을 `data`로 변경합니다.
    * `get(position)`: `position` 인덱스의 노드 값을 반환합니다.
3.  초기 수열을 입력받아 `append` 메서드를 이용해 연결 리스트(`arr`)를 생성합니다.
4.  총 `M`개의 명령어를 입력받아 반복문을 실행합니다.
5.  각 명령어의 종류('I', 'D', 'C')에 따라 `SinglyLinkedList`의 `insert`, `delete`, `update` 메서드를 각각 호출하여 수열을 편집합니다.
6.  모든 명령어 처리가 완료된 후, `arr.get(L)`을 호출하여 `L`번째 인덱스의 데이터를 가져옵니다.
7.  `get`을 시도하는 과정에서 `IndexError`가 발생하면 (이는 `L`이 최종 수열의 길이보다 크거나 같음을 의미), `-1`을 출력합니다.
8.  오류 없이 값을 가져왔다면 해당 값을 형식에 맞게 출력합니다.

### 💻 코드
* [5122.py](5122.py)

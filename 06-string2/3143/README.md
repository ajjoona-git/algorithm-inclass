# 3143. 가장 빠른 문자열 타이핑 | D4

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_65wkqsb4DFAWS&categoryId=AV_65wkqsb4DFAWS&categoryType=CODE&problemTitle=3143&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1/)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **문자열 처리(String Processing)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 전체 문자열 `full_str`과 키 문자열 `key_str`을 입력받습니다.
2.  Python의 내장 함수인 **`replace()`** 메서드를 사용하여 `full_str`에서 `key_str`이 나타나는 모든 부분을 하나의 문자(예: `-`)로 치환합니다.
3.  이렇게 치환된 문자열의 길이를 계산합니다. 이 길이는 전체 문자열을 구성하는 데 필요한 최소한의 키 입력 횟수와 동일합니다.
4.  최종 결과를 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [3143.py](3143.py)
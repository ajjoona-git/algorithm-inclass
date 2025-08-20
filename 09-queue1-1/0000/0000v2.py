# 연습문제. Queue
# deque 모듈 활용

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

print(queue.popleft())  # 1
print(queue.popleft())  # 2
print(queue.popleft())  # 3
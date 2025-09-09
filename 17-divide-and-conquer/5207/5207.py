# 5207. 이진 탐색

def binary_search(arr, l, r, key):
    global count
    if l == r:
        return
    
    mid = (l + r) // 2  # 중앙값을 기준으로
    if arr[mid] == key:
        return
    
    left = arr[l : mid]
    right = arr[mid+1 : r]



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arrA = list(map(int, input().split()))  # N개
    arrB = list(map(int, input().split()))  # M개
    count = 0
    
    print(f'#{tc} {count}')

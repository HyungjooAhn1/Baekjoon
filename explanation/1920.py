import sys
input = sys.stdin.readline
count = int(input())
A = list(map(int, input().split()))
A.sort()  # 이진탐색 위한 A 정렬
m = int(input())
nums = list(map(int, input().split()))
for num in nums:
    start = 0
    end = count-1
    exist = False
    while start <= end:
        mid = (start + end) // 2
        if num == A[mid]:
            exist = True
            print(1)
            break
        elif num > A[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if not exist:
        print(0)
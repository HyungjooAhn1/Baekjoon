import sys
import heapq
input = sys.stdin.readline
n = int(input())
ans = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(ans) == 0:
            print(0)
        else:
            print(heapq.heappop(ans)[1])
    else:
        heapq.heappush(ans, (abs(x), x))
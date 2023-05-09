import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int, input().split())
visited = [0] * (10**5+1)
visited[n] = 1
q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x == k:
        print(visited[k]-1)
        break
    for nx in [2*x, x-1, x+1]:
        if (0 <= nx <= 10**5) and (not visited[nx]):
            if nx == 2*x:
                visited[nx] = visited[x]
                q.appendleft(nx)
            else:
                visited[nx] = visited[x] + 1
                q.append(nx)
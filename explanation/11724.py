from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
for i in range(1,n+1):
    if visit[i] == 0:
        q = deque([i])
        while q:
            v = q.popleft()
            for nx in graph[v]:
                if visit[nx] == 0:
                    visit[nx] = 1
                    q.append(nx)
        cnt += 1
print(cnt)
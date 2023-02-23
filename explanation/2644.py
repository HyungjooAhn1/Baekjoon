import sys
from collections import deque
input = sys.stdin.readline
n = int(input())  # 전체 사람 수
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
q = deque([a])
while q:
    before = len(q)
    v = q.popleft()
    for i in graph[v]:
        if visit[i] == 0:
            visit[i] = visit[v] + 1
            q.append(i)
print(-1) if visit[b] == 0 else print(visit[b])
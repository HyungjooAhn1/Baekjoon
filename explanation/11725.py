import sys
from collections import deque
input = sys.stdin.readline
n = int(input())  # 노드의 개수
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visit[1] = 1
q = deque(graph[1])
for i in q:
    visit[i] = 1
while q:
    v = q.popleft()
    for nx in graph[v]:
        if visit[nx] == 0:
            visit[nx] = v
            q.append(nx)
for i in visit[2:]:
    print(i)
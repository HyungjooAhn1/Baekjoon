# BFS
from collections import deque
n = int(input())  # 컴퓨터 수
m = int(input())  # 직접 연결된 컴퓨터 쌍의 수
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]  # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]] 이런 식으로 컴퓨터 연결 파악
visited[1] = 1
Q = deque([1])
while Q:
    c = Q.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            Q.append(nx)
            visited[nx] = 1
print(sum(visited)-1)
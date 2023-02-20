from collections import deque
n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visit_b = [0] * (n+1)
visit_d = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
# DFS
def dfs(v):
    visit_d[v] = 1
    print(v, end=' ')
    for i in range(1,n+1):
        if visit_d[i] == 0 and graph[v][i] == 1:
            dfs(i)
# BFS
def bfs(v):
    q = deque()
    q.append(v)
    visit_b[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1,n+1):
            if visit_b[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_b[i] = 1
dfs(v)
print('')
bfs(v)
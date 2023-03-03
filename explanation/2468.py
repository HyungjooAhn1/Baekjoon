from collections import deque
n = int(input())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    graph.append(list(map(int, input().split())))
min_graph = []
max_graph = []
for i in graph:
    min_graph.append(min(i))
    max_graph.append(max(i))
min_graph = min(min_graph)
max_graph = max(max_graph)
safe = []
if min_graph == max_graph:
    print(1)
else:
    for k in range(1, max_graph):
        bool_graph = [[False] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] > k and not bool_graph[i][j]:
                    q = deque()
                    q.append((i,j))
                    bool_graph[i][j] = True
                    while q:
                        x,y = q.popleft()
                        for l in range(4):
                            nx = x + dx[l]
                            ny = y + dy[l]
                            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                                continue
                            if graph[nx][ny] > k and not bool_graph[nx][ny]:
                                q.append((nx,ny))
                                bool_graph[nx][ny] = True
                    cnt += 1
        safe.append(cnt)
    print(max(safe))
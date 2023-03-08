import sys
from collections import deque
input = sys.stdin.readline
m,n,h = map(int, input().split())
graph = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int, input().split())))
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i,j,k))
def bfs():
    while q:
        z,y,x = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if (0 <= nx < m) and (0 <= ny < n) and (0 <= nz < h) and (graph[nz][ny][nx] == 0):
                graph[nz][ny][nx] = graph[z][y][x] + 1
                q.append((nz, ny, nx))
bfs()
res = 0
for i in graph:
    for j in i:
        if 0 in j:
            print(-1)
            exit()
        res = max(res, max(j))
print(res-1)
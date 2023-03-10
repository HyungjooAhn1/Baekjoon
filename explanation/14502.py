import copy
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
empty = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i,j))
cnt = 0
for a in combinations(empty, 3):
    graph_new = copy.deepcopy(graph)
    for x, y in a:
        graph_new[x][y] = 1
    virus = deque()
    for i in range(n):
        for j in range(m):
            if graph_new[i][j] == 2:
                virus.append((i,j))
    while virus:
        x,y = virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and graph_new[nx][ny] == 0:
                graph_new[nx][ny] = 2
                virus.append((nx,ny))
    safe_cnt = 0
    for row in graph_new:
        safe_cnt += row.count(0)
    cnt = max(cnt, safe_cnt)
print(cnt)
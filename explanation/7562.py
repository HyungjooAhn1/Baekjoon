import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,-1,1]
for _ in range(t):
    l = int(input())
    graph = [[0] * l for i in range(l)]
    sx, sy = map(int, input().split())  # 시작점
    ex, ey = map(int, input().split())  # 끝점
    graph[sx][sy] = 1
    q = deque()
    q.append((sx,sy))
    while q:
        x,y = q.popleft()
        if x == ex and y == ey:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < l) and (0 <= ny < l) and graph[nx][ny] == 0:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
    print(graph[ex][ey]-1)
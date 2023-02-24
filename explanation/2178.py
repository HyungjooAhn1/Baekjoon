import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().rstrip())))
dx = [-1,1,0,0]  # x축 방향
dy = [0,0,-1,1]  # y축 방향
q = deque()
q.append((0,0))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if maze[nx][ny] == 0:
            continue

        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            q.append((nx,ny))
print(maze[n-1][m-1])
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    maze = []
    for _ in range(n):
        maze.append([0] * m)
    for _ in range(k):
        x, y = map(int, input().split())
        maze[y][x] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                q = deque()
                q.append((i, j))
                maze[i][j] = 0
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if maze[nx][ny] == 1:
                            maze[nx][ny] = 0
                            q.append((nx, ny))
                cnt += 1
    print(cnt)
from collections import deque
m,n,k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    sy, sx, ey, ex = map(int, input().split())
    for i in range(sx, ex):
        for j in range(sy, ey):
            graph[i][j] = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
nums = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            q = deque()
            q.append((i,j))
            graph[i][j] = 1
            num = 1
            while q:
                y,x = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if (0 <= nx < n) and (0 <= ny < m) and graph[ny][nx] == 0:
                        graph[ny][nx] = 1
                        q.append((ny,nx))
                        num += 1
            cnt += 1
            nums.append(num)
nums.sort()
print(cnt)
print(*nums)
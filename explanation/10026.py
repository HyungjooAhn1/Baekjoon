from collections import deque
def bfs(i,j):
    q.append((i, j))
    visit[i][j] = True
    while q:
        x, y = q.popleft()
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == graph[x][y] and not visit[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = True

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
visit = [[False] * n for _ in range(n)]
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt1 = 0
cnt2 = 0
# 적록색약 아닌 사람
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i,j)
            cnt1 += 1
# 적록색약인 사람
visit = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i,j)
            cnt2 += 1
print(cnt1, cnt2)
import sys
input = sys.stdin.readline
r,c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list((input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 1

def bfs(x, y):
    global answer
    q = set([(x, y, graph[x][y])])
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((0 <= nx < r) and (0 <= ny < c)) and (graph[nx][ny] not in ans):
                q.add((nx,ny,ans + graph[nx][ny]))
                answer = max(answer, len(ans)+1)
bfs(0,0)
print(answer)
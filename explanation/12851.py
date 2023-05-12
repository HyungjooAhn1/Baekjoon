from collections import deque
n,k = map(int, input().split())
visited = [[-1,0] for _ in range(100001)]
visited[n][0] = 0
visited[n][1] = 1
q = deque([n])
while q:
    x = q.popleft()
    for nx in [2*x,x-1,x+1]:
        if 0 <= nx <= 100000:
            if visited[nx][0] == -1:
                visited[nx][0] = visited[x][0] + 1
                visited[nx][1] = visited[x][1]
                q.append(nx)
            elif visited[nx][0] == visited[x][0] + 1:
                visited[nx][1] += visited[x][1]
print(visited[k][0])
print(visited[k][1])
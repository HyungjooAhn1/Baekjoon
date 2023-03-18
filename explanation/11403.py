from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
answer = [[0] * n for i in range(n)]
for i in range(0,n):
    q = deque()
    q.append(i)
    visit = [0 for _ in range(n+1)]
    while q:
        a = q.popleft()
        for j in range(n):
            if graph[a][j] == 1 and visit[j+1] == 0:
                q.append(j)
                visit[j+1] = 1
                answer[i][j] = 1
for i in answer:
    print(*i)
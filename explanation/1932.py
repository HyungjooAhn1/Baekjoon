n = int(input())
graph = [[0] for _ in range(n)]
for i in range(n):
    graph[i] += list(map(int, input().split()))
    graph[i].append(0)
for i in range(1,n):
    a = len(graph[i])
    for j in range(1,a-1):
        graph[i][j] = max(graph[i-1][j], graph[i-1][j-1]) + graph[i][j]
print(max(graph[n-1]))
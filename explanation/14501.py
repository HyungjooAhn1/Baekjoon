n = int(input())
graph = []
for _ in range(n):
    t,p = map(int, input().split())
    graph.append([t,p])
dp = [0 for _ in range(n+1)]
for i in range(n):
    for j in range(i+graph[i][0],n+1):
        if dp[j] < dp[i] + graph[i][1]:
            dp[j] = dp[i] + graph[i][1]
print(dp[-1])
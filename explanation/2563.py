n = int(input())
graph = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x-1,x+9):
        for j in range(y-1,y+9):
            graph[i][j] = 1
ans = 0
for i in range(100):
    ans += sum(graph[i])
print(ans)
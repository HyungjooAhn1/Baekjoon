from itertools import combinations
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append([i,j])
        elif graph[i][j] == 1:
            house.append([i,j])
ans = []
for chi in combinations(chicken,m):
    h = 0
    for i1,j1 in house:
        chi_len = 999
        for k in range(m):
            chi_len = min(chi_len, abs(i1 - chi[k][0]) + abs(j1 - chi[k][1]))
        h += chi_len
    ans.append(h)
print(min(ans))

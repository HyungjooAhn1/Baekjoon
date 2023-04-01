# 냅색 알고리즘
n,k = map(int, input().split())
bag = [[0,0]]
for _ in range(n):
    bag.append(list(map(int, input().split())))
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        w,v = bag[i][0], bag[i][1]
        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])
print(knapsack[n][k])
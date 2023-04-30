n,m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
def dfs(x):
    if len(ans) == m:
        print(*ans)
    else:
        rem = 0
        for i in range(x,n):
            if seq[i] != rem:
                rem = seq[i]
                ans.append(seq[i])
                dfs(i)
                ans.pop()
ans = []
dfs(0)
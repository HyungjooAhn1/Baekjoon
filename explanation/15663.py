import sys
input = sys.stdin.readline
n,m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
visited = [False] * n
ans = []
def dfs(x):
    if len(ans) == m:
        print(*ans)
    else:
        rem = 0
        for i in range(n):
            if not visited[i] and rem != seq[i]:
                visited[i] = True
                ans.append(seq[i])
                rem = seq[i]
                dfs(i)
                visited[i] = False
                ans.pop()
dfs(-1)
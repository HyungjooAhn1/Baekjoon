import sys
input = sys.stdin.readline
n,m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
def dfs(x):
    if len(ans) == m:
        print(*ans)
    else:
        for i in seq:
            if i not in ans:
                ans.append(i)
                dfs(i)
                ans.pop()
ans = []
dfs(1)
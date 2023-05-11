from collections import deque
n,k = map(int, input().split())
visited = [0] * 100001
move = [0] * 100001
visited[n] = 1
q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x == k:
        break
    for i in [x-1, x+1, 2*x]:
        if (0 <= i <= 100000) and not visited[i]:
            visited[i] = visited[x] + 1
            move[i] = x
            q.append(i)
print(visited[k]-1)
ans = []
for _ in range(visited[k]):
    ans.append(x)
    x = move[x]
print(*ans[::-1])
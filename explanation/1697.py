from collections import deque
n,k = map(int, input().split())
dist = [0] * (10**5 + 1)
q = deque()
q.append(n)
while q:
    a = q.popleft()
    if a == k:
        break
    for nx in [a-1, a+1, 2*a]:
        if 0 <= nx <= 10**5 and not dist[nx]:
            dist[nx] = dist[a] + 1
            q.append(nx)
print(dist[k])
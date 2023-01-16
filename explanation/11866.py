from collections import deque
n,k = map(int, input().split())
Josephus = deque()
for i in range(1,n+1):
    Josephus.append(i)
print('<', end='')
while Josephus:
    for _ in range(0,k-1):
        Josephus.append(Josephus[0])
        Josephus.popleft()
    print(Josephus.popleft(), end='')
    if Josephus:
        print(', ', end='')
print('>')
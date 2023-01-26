from collections import deque
n,k = map(int, input().split())
queue = deque()
for i in range(1,n+1):
    queue.append(i)
print('<', end='')
while len(queue) > 0:
    for _ in range(k-1):
        queue.append(queue[0])
        queue.popleft()
    if len(queue) > 1:
        print(queue.popleft(), end='')
        print(',', end=' ')
    else:
        print(queue.popleft(), end='')
print('>')
from collections import deque
n,m = map(int, input().split())
num = list(map(int, input().split()))
queue = deque()
for i in range(n):
    queue.append(i+1)
cnt = 0
for i in num:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue)/2:
                while queue[0] != i:
                    queue.append(queue[0])
                    queue.popleft()
                    cnt += 1
            else:
                while queue[0] != i:
                    queue.appendleft(queue[-1])
                    queue.pop()
                    cnt += 1
print(cnt)
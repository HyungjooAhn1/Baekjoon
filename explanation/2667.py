import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
house_num = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt_each = 1
            q = deque()
            q.append((i,j))
            graph[i][j] = 0
            while q:
                x,y = q.popleft()
                for l in range(4):
                    nx = x + dx[l]
                    ny = y + dy[l]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if graph[nx][ny] == 1:
                        q.append((nx,ny))
                        graph[nx][ny] = 0
                        cnt_each += 1
            house_num.append(cnt_each)
house_num.sort()
print(len(house_num))
for i in house_num:
    print(i)
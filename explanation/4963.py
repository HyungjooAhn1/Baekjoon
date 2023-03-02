import sys
from collections import deque
input = sys.stdin.readline
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    else:
        graph = []
        for _ in range(h):
            graph.append(list(map(int, input().split())))
        dx = [-1,1,0,0,1,1,-1,-1]
        dy = [0,0,-1,1,-1,1,-1,1]
        cnt = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    q = deque()
                    q.append((i,j))
                    graph[i][j] = 0
                    while q:
                        x,y = q.popleft()
                        for l in range(8):
                            nx = x + dx[l]
                            ny = y + dy[l]
                            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                                continue
                            if graph[nx][ny] == 1:
                                graph[nx][ny] = 0
                                q.append((nx,ny))
                    cnt += 1
        print(cnt)
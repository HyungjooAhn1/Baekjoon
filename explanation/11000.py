import heapq
n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int, input().split())))
time = sorted(time, key=lambda x: x[0])
room = []
heapq.heappush(room, time[0][1])
for i in range(1,n):
    if time[i][0] < room[0]:
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time[i][1])
print(len(room))
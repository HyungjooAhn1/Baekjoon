n = int(input())  # 회의의 수
cfs = []
for _ in range(n):
    s,e = map(int, input().split())
    cfs.append([s,e])
cfs.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end = cfs[0][1]
for i in range(1,n):
    if cfs[i][0] >= end:
        end = cfs[i][1]
        cnt += 1
print(cnt)
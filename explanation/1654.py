k,n = map(int, input().split())
LAN = []
for _ in range(k):
    LAN.append(int(input()))
start = 1
end = max(LAN)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for j in LAN:
        cnt += j // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
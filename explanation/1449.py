n, l = map(int, input().split())
water = list(map(int, input().split()))
water.sort()
start = water[0]
end = water[0] + l
cnt = 1
for i in range(1,n):
    if start <= water[i] < end:
        continue
    else:
        start = water[i]
        end = water[i] + l
        cnt += 1
print(cnt)
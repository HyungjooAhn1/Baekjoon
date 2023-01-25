n = int(input())
p = list(map(int, input().split()))
p.sort()
time = 0
for i in range(n):
    time += (n-i) * p[i]
print(time)
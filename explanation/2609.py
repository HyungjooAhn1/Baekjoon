list1 = list(map(int, input().split()))
a,b = min(list1), max(list1)
for i in range(a,0,-1):
    if (a % i == 0) & (b % i == 0):
        print(i)
        break
print(int(i * (a/i) * (b/i)))
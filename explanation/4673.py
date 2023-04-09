list1 = [0 for _ in range(10001)]
for i in range(1,10001):
    a = i
    for j in str(i):
        a += int(j)
    if a <= 10000 and list1[a] == 0:
        list1[a] = 1
for i in range(1,10001):
    if list1[i] == 0:
        print(i)
n = list(map(int, input()))
n.sort(reverse=True)
if (0 not in n) or (sum(n) % 3 != 0):
    print(-1)
else:
    for i in n:
        print(i, end='')
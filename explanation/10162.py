t = int(input())
if t % 10 != 0:
    print(-1)
else:
    for time in [300, 60, 10]:
        print(t // time, end=' ')
        t %= time
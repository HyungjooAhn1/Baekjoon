import sys
input = sys.stdin.readline
a,b = map(int, input().split())
cnt = 1
while b != a:
    cnt += 1
    same = b
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    if same == b:
        print(-1)
        break
else:
    print(cnt)
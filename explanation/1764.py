n,m = map(int, input().split())
listen = set()
see = set()
for _ in range(n):
    listen.add(input())
for _ in range(m):
    see.add(input())
never = sorted(list(listen & see))
print(len(never))
for i in never:
    print(i)
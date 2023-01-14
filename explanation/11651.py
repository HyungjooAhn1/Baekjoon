import sys
input = sys.stdin.readline
count = int(input())
coord = []
for _ in range(count):
    x,y = map(int, input().split())
    coord.append((int(x), int(y)))
coord = sorted(coord, key = lambda x: (x[1], x[0]))
for x,y in coord:
    print(x, y)
import sys
input = sys.stdin.readline
coord = []
x,y = [],[]
for _ in range(3):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
    coord.append([a,b])
for i in x:
    for j in y:
        if [i,j] not in coord:
            print(i,j)
            break
count = int(input())
weight = []
height = []
for _ in range(count):
    w, h = map(int, input().split())
    weight.append(w)
    height.append(h)
for i in range(count):
    rank = 0
    for j in range(count):
        if (weight[i] < weight[j]) & (height[i] < height[j]):
            rank += 1
    print(rank + 1, end=' ')
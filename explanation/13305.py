n = int(input())
road = list(map(int, input().split()))
l = list(map(int, input().split()))
answer = 0
cost = l[0]
for i in range(n-1):
    if l[i] < cost:
        cost = l[i]
    answer += cost * road[i]
print(answer)
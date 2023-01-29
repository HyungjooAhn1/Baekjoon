n = int(input())
scores = []
for _ in range(n):
    scores.append((input().split()))
scores = sorted(scores, key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in scores:
    print(i[0])
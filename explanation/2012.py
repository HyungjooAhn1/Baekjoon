import sys
input = sys.stdin.readline
n = int(input())
rank = []
for _ in range(n):
    rank.append(int(input()))
rank.sort()
answer = 0
for i in range(n):
    answer += abs(rank[i] - (i+1))
print(answer)
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
seq = list(map(int, input().split()))
prefix = [0]
temp = 0
for i in seq:
    temp += i
    prefix.append(temp)
for _ in range(m):
    i,j = map(int, input().split())
    print(prefix[j] - prefix[i-1])
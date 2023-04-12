import sys
input = sys.stdin.readline
n = int(input())
xs = list(map(int, input().split()))
seq = sorted(set(xs))
dic = {seq[i] : i for i in range(len(seq))}
for i in xs:
    print(dic[i], end=' ')
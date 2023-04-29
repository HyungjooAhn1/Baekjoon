import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
n,m = map(int, input().split())
seq = [i for i in range(1,n+1)]
for i in combinations_with_replacement(seq,m):
    print(*i)
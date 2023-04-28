import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int, input().split())
list1 = [i for i in range(1,n+1)]
for i in combinations(list1,m):
    print(*i)
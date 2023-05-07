import sys
from collections import Counter
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    wear = []
    for _ in range(n):
        a,b = input().split()
        wear.append(b)
    ans = 1
    result = Counter(wear)
    for i in result:
        ans *= result[i] + 1
    print(ans-1)
import sys
import math
input = sys.stdin.readline
n,s = map(int, input().split())
bro = list(map(int, input().split()))
for i in range(n):
    bro[i] = abs(bro[i] - s)
print(math.gcd(*bro))
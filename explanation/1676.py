import math
n = int(input())
s = str(math.factorial(n))[::-1]
if s[0] == '0':
    i = 0
    while s[i] == '0':
        i += 1
    print(i)
else:
    print(0)

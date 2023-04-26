import sys
input = sys.stdin.readline
m = int(input())
S = set()
for _ in range(m):
    str1 = input().split()
    if str1[0] == 'add':
        if int(str1[1]) in S:
            continue
        else:
            S.add(int(str1[1]))
    elif str1[0] == 'remove':
        if int(str1[1]) in S:
            S.remove(int(str1[1]))
        else:
            continue
    elif str1[0] == 'check':
        print(1) if int(str1[1]) in S else print(0)
    elif str1[0] == 'toggle':
        S.remove(int(str1[1])) if int(str1[1]) in S else S.add(int(str1[1]))
    elif str1[0] == 'all':
        S = set(range(1,21))
    elif str1[0] == 'empty':
        S = set()
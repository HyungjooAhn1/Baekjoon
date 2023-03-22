import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    list1 = [0] * 41
    list1[n] = 1
    for i in range(40,1,-1):
        if list1[i] > 0:
            list1[i-1] += list1[i]
            list1[i-2] += list1[i]
            list1[i] = 0
    print(list1[0], list1[1])
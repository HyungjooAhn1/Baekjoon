import sys
num = int(sys.stdin.readline())
list1 = []
for i in range(num):
    list1.append(int(sys.stdin.readline()))
for i in sorted(list1):
    print(i)
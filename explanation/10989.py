import sys
count = int(sys.stdin.readline())  # 메모리 할당량 낮춰줌
list1 = [0] * 10001
for i in range(count):
    b = int(sys.stdin.readline())
    list1[b] += 1

for i in range(10001):
    if list1[i] != 0:
        for j in range(list1[i]):
            print(i)
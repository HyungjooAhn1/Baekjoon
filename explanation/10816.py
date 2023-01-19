import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
all = [0] * 20000001  # 범위가 -10,000,000 ~ 10,000,000
for card in cards:
    all[card] += 1
m = int(input())
numbers = list(map(int, input().split()))
for number in numbers:
    if number == numbers[-1]:
        print(all[number])
    else:
        print(all[number], end=' ')
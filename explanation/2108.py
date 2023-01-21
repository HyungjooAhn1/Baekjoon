import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
numbers.sort()
print(round(sum(numbers) / n))  # 산술평균
print(numbers[n//2])  # 중앙값
# 최빈값
mode = Counter(numbers).most_common(2)  # 빈도수가 높은 두 개
if len(numbers) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])
print(numbers[-1] - numbers[0])  # 범위
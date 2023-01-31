import math
n = int(input())
squares = [[] for _ in range(n)]
a = 0  # 가로 2인 상자 개수
b = 0
while a*2 <= n:
    squares[b] += [n-a*2]  # 가로 1인 상자 개수
    squares[b] += [a]  # 가로 2인 상자 개수
    a += 1
    b += 1
answer = 0
for square in squares:
    if len(square) != 0:
        answer += math.factorial(square[0] + square[1]) // (math.factorial(square[0]) * math.factorial(square[1]))
print(answer % 10007)

# 초간단 풀이
# s = [0, 1, 2]
# for i in range(3, 1001):
#   s.append(s[i - 2] + s[i - 1])
# n = int(input())
# print(s[n] % 10007)
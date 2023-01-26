n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
answer = 0
for i in range(n):
    answer += A[i] * max(B)
    B.pop(B.index(max(B)))
print(answer)
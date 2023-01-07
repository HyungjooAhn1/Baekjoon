a,b = map(int, input().split())
if a-b < b:
    b = a-b
answer = 1
for i in range(a,a-b,-1):
    answer *= i
for i in range(b,1,-1):
    answer /= i
print(int(answer))
t = int(input())
for _ in range(t):
    c = int(input())
    answer = []
    for cent in [25,10,5,1]:
        answer.append(c // cent)
        c %= cent
    print(*answer)
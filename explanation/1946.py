import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    score = []
    for _ in range(n):
        a,b = map(int, input().split())
        score.append([a,b])
    score.sort()
    top = 0
    answer = 1
    for i in range(1,n):
        if score[i][1] < score[top][1]:
            top = i
            answer += 1
    print(answer)
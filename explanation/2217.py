n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope.sort()
answer = []
for i in range(n):
    answer.append(rope[i] * (len(rope)-i))
print(max(answer))
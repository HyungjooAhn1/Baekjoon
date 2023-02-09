import heapq
n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))
answer = 0
if len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        a = heapq.heappop(cards) + heapq.heappop(cards)
        answer += a
        heapq.heappush(cards, a)
    print(answer)
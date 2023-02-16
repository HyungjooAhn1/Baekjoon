n = int(input())  # 가지고 있는 카드 개수
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))
cards.sort()
for number in numbers:
    start = 0
    end = n-1
    exist = False
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == number:
            exist = True
            break
        elif cards[mid] < number:
            start = mid + 1
        else:
            end = mid -1
    print(1, end=' ') if exist else print(0, end=' ')
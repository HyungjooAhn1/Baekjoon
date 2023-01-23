numbers = list(map(int, input()))
numbers.sort(reverse=True)
for i in numbers:
    print(i, end='')
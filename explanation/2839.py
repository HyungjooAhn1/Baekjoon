kg = int(input())
bag = 0
while kg >= 0:
    if kg % 5 == 0:
        bag += kg // 5
        break
    kg -= 3
    bag += 1
print(-1) if kg < 0 else print(bag)
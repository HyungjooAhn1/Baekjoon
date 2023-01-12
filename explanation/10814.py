count = int(input())
join = []
for _ in range(count):
    age, name = input().split()
    age = int(age)
    join.append((age, name))
join = sorted(join, key = lambda x: x[0])
for age, name in join:
    print(age, name)
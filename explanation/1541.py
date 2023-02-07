equation = input().split('-')
answer = sum([int(i) for i in equation[0].split('+')])
for i in equation[1:]:
    for j in i.split('+'):
        answer -= int(j)
print(answer)
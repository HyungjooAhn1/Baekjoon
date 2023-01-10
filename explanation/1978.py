num = int(input())
list1 = list(map(int, input().split()))
answer = 0
for i in list1:
    list2 = []
    for j in range(1,i+1):
        if i%j == 0:
            list2.append(j)
    if len(list2) == 2:
        answer += 1
print(answer)
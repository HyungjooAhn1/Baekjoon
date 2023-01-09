num = int(input())
list1 = []
for i in range(num):
    word = input()
    if word in list1:
        continue
    else:
        list1.append(word)
list1 = sorted(list1, key = lambda x: (len(x), x))
for i in list1:
    print(i)

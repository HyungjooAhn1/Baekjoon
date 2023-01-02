a,b = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = []
for i in range(a-2):
    for j in range(i+1,a-1):
        for l in range(j+1,a):
            if list1[i]+list1[j]+list1[l] <= b:
                list2.append(b-(list1[i]+list1[j]+list1[l]))

list2 = sorted(list2, key=abs)
print(b-list2[0])
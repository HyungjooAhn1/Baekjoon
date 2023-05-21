s = input()
ans = set()
l = len(s)
for i in range(1,l+1):
    for j in range(l):
        ans.add(s[j:j+i])
print(len(ans))
s = input()
t = input()
ans = []
for i in t:
    ans.append(i)
for i in range(len(t)-1,len(s)-1,-1):
    if ans[i] == 'A':
        ans.pop()
    else:
        ans.pop()
        ans.reverse()
if s == ''.join(ans):
    print(1)
else:
    print(0)

word = input()
bomb = input()
n = len(bomb)
ans = []
for i in word:
    ans.append(i)
    if ''.join(ans[-n:]) == bomb:
        for _ in range(n):
            ans.pop(-1)
print('FRULA') if len(ans) == 0 else print(''.join(ans))
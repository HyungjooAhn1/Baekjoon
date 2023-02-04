s = input()
cnt0 = 0
cnt1 = 0
for i in s.split('0'):
    if i != '':
        cnt0 += 1
for i in s.split('1'):
    if i != '':
        cnt1 += 1
print(min(cnt0, cnt1))
money = 1000 - int(input())
cnt = 0
ens = [500, 100, 50, 10, 5, 1]
for en in ens:
    if money >= en:
        cnt += money // en
        money %= en
    if money == 0:
        break
print(cnt)
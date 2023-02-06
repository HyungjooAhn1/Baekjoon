n = 1
while True:
    l,p,v = map(int, input().split())
    if l == p == v== 0:
        break
    else:
        print(f'Case {n}: {(v//p)*l + min(v%p,l)}')
        n += 1
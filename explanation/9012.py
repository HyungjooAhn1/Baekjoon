t = int(input())
for _ in range(t):
    ps = input()
    ps_list = []
    for i in ps:
        if i == '(':
            ps_list.append(i)
        else:
            if '(' in ps_list:
                ps_list.pop()
            else:
                ps_list.append(i)
    if len(ps_list) == 0:
        print('YES')
    else:
        print('NO')

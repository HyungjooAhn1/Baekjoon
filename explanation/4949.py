while True:
    strings = input()
    if strings == '.':
        break
    elif strings[-1] != '.':
        while strings[-1] != '.':
            strings += input()
    else:
        str_list = []
        for str in strings:
            if str in '([':
                str_list.append(str)
            elif str == ')':
                if not str_list or str_list[-1] == '[':
                    str_list.append(str)
                    break
                elif str_list[-1] == '(':
                    str_list.pop(-1)
            elif str == ']':
                if not str_list or str_list[-1] == '(':
                    str_list.append(str)
                    break
                elif str_list[-1] == '[':
                    str_list.pop(-1)
        if len(str_list) == 0:
            print('yes')
        else:
            print('no')
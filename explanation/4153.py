while True:
    list1 = list(map(int, input().split()))
    list1.sort()  # 오름차순 정렬
    if list1[0] == list1[1] == list1[2] == 0:
        break
    else:
        if list1[0]**2 + list1[1]**2 == list1[2]**2:
            print('right')
        else:
            print('wrong')
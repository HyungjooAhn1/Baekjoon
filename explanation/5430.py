from collections import deque
t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    arr = deque(input()[1:-1].split(','))
    rev, front, back = 0, 0, len(arr) - 1
    flag = 0
    if n == 0:
        arr = []
        front = 0
        back = 0
    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(arr) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(arr) + "]")
        else:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
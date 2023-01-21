n = int(input())
number = 665
cnt = 0
while True:
    number += 1
    if '666' in str(number):
        cnt += 1
    if cnt == n:
        break
print(number)
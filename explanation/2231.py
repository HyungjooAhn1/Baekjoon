num = int(input())
for i in range(num):
    num_sum = i
    for j in range(len(str(i))):
        num_sum += int(str(i)[j])
    if num_sum == num:
        print(i)
        break
    if i == num-1:
        print(0)

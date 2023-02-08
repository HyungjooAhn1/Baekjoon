a = input()
print(sum([int(i) for i in a.replace('6','5').split()]), end=' ')
print(sum([int(i) for i in a.replace('5','6').split()]))
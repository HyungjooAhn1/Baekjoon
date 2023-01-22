cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
for i in cro:
    word = word.replace(i,'+')
print(len(word))
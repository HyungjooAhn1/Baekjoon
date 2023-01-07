length = int(input())
list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet = input()
answer = 0
for i in range(length):
    answer += (list1.index(alphabet[i]) + 1)*(31**i)
print(answer % 1234567891)
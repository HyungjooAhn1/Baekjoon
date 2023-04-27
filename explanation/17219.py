n,m = map(int, input().split())
dic = {}
for _ in range(n):
    i,j = input().split()
    dic[i] = j
for _ in range(m):
    i = input()
    print(dic[i])
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
pokemon_name = {}
pokemon_num = {}
for i in range(n):
    a = input().strip()
    pokemon_name[a] = i+1
    pokemon_num[i+1] = a
for _ in range(m):
    a = input().strip()
    if a.isdigit() == True:
        print(pokemon_num[int(a)])
    else:
        print(pokemon_name[a])
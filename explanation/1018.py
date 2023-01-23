n,m = map(int, input().split())
chess = []
change = []
for _ in range(n):
    chess.append(input())
for i in range(n-7):
    for j in range(m-7):
        W = 0
        B = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k + l) % 2 == 0:
                    if chess[k][l] == 'W':
                        W += 1
                    elif chess[k][l] == 'B':
                        B += 1
                else:
                    if chess[k][l] == 'B':
                        W += 1
                    elif chess[k][l] == 'W':
                        B += 1
        change.append(min(W,B))
print(min(change))
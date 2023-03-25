n = int(input())
seq = [0,1] + [0 for _ in range(89)]
if n == 1:
    print(seq[n])
else:
    for i in range(2,n+1):
        seq[i] = seq[i-1] + seq[i-2]
    print(seq[n])
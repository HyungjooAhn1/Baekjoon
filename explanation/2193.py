n = int(input())
seq = [0 for _ in range(90)]
seq[0] = 1
seq[1] = 1
for i in range(2,90):
    seq[i] = seq[i-1] + seq[i-2]
print(seq[n-1])
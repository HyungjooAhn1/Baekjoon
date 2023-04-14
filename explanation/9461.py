t = int(input())
seq = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0 for _ in range(90)]
for i in range(10,100):
    seq[i] = seq[i-1] + seq[i-5]
for _ in range(t):
    n = int(input())
    print(seq[n-1])
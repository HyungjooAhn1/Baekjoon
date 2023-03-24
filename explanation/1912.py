n = int(input())
seq = list(map(int, input().split()))
dp = [seq[0]]
for i in range(n-1):
    dp.append(max(dp[i]+seq[i+1], seq[i+1]))
print(max(dp))
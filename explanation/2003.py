# 투 포인터
n,m = map(int, input().split())
seq = list(map(int, input().split()))
cnt = 0
start = 0
end = 0
while start <= n-1:
    if sum(seq[start:end+1]) < m:
        end += 1
        if end > n:
            break
    elif sum(seq[start:end+1]) == m:
        cnt += 1
        start += 1
    else:
        start += 1
print(cnt)
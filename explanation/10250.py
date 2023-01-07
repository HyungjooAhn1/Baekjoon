num = int(input())
for i in range(num):
    h,w,n = map(int, input().split())
    if n % h == 0:
        print(100*h + (n // h))
    else:
        print(100*(n % h) + (n // h + 1))
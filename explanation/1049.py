n,m = map(int, input().split())
package = []
single = []
for _ in range(m):
    a,b = map(int, input().split())
    package.append(a)
    single.append(b)
p,s = n // 6, n % 6
print(min(package + [6*i for i in single])*p + min(package + [s*i for i in single]))
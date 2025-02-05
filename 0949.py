n, a, b = map(int, input().split())

for i in range(n-1):
    p = b-a
    b = a
    a=p
print(a,b)
a,b,c,d = map(int,input().split())

data = []
for x in range(-1000,1000):
    value = a*(x**3)+b*(x**2)+c*x+d
    if value == 0:
        data.append(x)

d = set(data)
data = []
for i in d:
    data.append(i)
data.sort()
print(*data)
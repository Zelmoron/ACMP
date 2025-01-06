n = int(input())





a = n-1
b = n+1
c = n+8
d = n-8
data = []

if n%8==0:
    b = 0
if (n-1)%8==0:
    a = 0

if a >0 and a < 65:
   data.append(a)
if b >0 and b < 65:
    data.append(b)

if c >0 and c < 65:
    data.append(c)

if d >0 and d < 65:
    data.append(d)

data.sort()
print(*data)
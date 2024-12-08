n = int(input())

data = []

for i in range(n):
    value = int(input())
    data.append(value)
    
zero = data.count(0)
one = data.count(1)
print(zero if zero < one else one)
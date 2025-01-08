n = int(input())

result = []

while n!=0:
    o = n%2
    s = int(n/2)
    n=s
    result.append(o)

print(sum(result))
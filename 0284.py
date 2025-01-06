n = int(input())



data = [int(i) for i in input().split()]
result = []

m = int(input())

for i in range(m):
    i,j = map(int,input().split())


    result.append(data[i-1:j])


for i in result:
    print(*i)
n,m = map(int,input().split())
data=[]
r_data=[]
count = 0
for i in range(n):
    data.append(input())
space = input()
for i in range(n):
    r_data.append(input())


for i in range(n):
    for j in range(m):
        if data[i][j] == r_data[i][j]:
            count+=1

print(count)
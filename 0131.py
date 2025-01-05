n = int(input())

dataArr = []

for i in range(n):
    data = [int(i) for i in input().split()]
    dataArr.append(data)
    
count = 0
mn = -1000
mxc = -1
for v in dataArr:
    count+=1
    if v[1] == 1:
        
        if v[0]>mn:
            mn = v[0]
            mxc = count


print(mxc)
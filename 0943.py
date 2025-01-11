a,b,c,d = map(int,input().split())


count=-1
result = []
data = []
for i in range(a):
    for j in range(b):
        count+=1
        data.append(count)
    if i%2==1:
        data.sort(reverse=True)    
    
    result.append(data)
    data=[]
print(result[c-1][d-1])
data = ["G","C","V"]    
for i in range(int(input())):
    data[1],data[-1] =data[-1],data[1]
    data[0],data[1] = data[1],data[0]

print(*data,sep="")
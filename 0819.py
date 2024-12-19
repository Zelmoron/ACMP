data = [int(i) for i in input().split()]


sum =0
for i in range(len(data)):
    for j in range(i+1,len(data)):
        
        sum+=data[i]*data[j]

print(sum*2,data[0]*data[1]*data[2])
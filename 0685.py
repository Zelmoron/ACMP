data = [int(i) for i in input().split()]




price =  [data[0],data[1],data[2]]
price.sort(reverse=True)


data = data[3:]
data.sort(reverse=True)
# print(price,data
print(price[0]*data[0]+data[1]*price[1]+data[2]*price[2])
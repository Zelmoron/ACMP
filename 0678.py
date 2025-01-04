s = input()

data = [1,0,0]


map = {"A":"01","B":"12","C":"02"}



for i in s:
    data[int(map[i][0])],data[int(map[i][1])]=data[int(map[i][1])],data[int(map[i][0])]


print(data.index(1)+1)
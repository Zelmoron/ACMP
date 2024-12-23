data = [int(i) for i in input().split()]



if data[0] >= data[1]:
    print(12-(data[0]-data[1]))
else:
    print(data[1]-data[0])
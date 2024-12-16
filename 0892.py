n = int(input())


data = ["Autumn","Winter","Spring","Summer"]


if n >0 and n <=2 or n == 12:
    print(data[1])
elif n > 2 and n < 6:
    print(data[2])
elif n > 5 and n < 9:
    print(data[3])
elif n > 8 and n<12:
    print(data[0])
else:
    print("Error")
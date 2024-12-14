data = [int(i) for i in input().split()]

while True:
    if data[0] + data[1] == data[2]:
        print("YES")
        break
    elif data[0] + data[2] == data[1]:
        print("YES")
        break
    elif data[1] + data[0] == data[2]:
        print("YES")
        break
    elif data[1] + data[2] == data[0]:
        print("YES")
        break
    elif data[2] + data[0] == data[1]:
        print("YES")
        break
    elif data[2] + data[1] == data[0]:
        print("YES")
        break
    else:
        print("NO")
        break
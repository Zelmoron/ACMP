data = "qwertyuiopasdfghjklzxcvbnm"



s = input()

for i in range(len(data)):
    if s == data[i]:
        if i == len(data)-1:
            print(data[0])
            break
        print(data[i+1])
        break

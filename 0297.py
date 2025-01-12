n = input()


data = {"8":2,"6":1,"9":1,"0":1}

count = 0

for i in n:
    try:
        if data[i] >0:
            count += data[i]
    except:
        continue
print(count)
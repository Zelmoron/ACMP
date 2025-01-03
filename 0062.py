s = input()


data = "ABCDEFGH"


alpha = s[0]
number = int(s[1])

flag  = True
if number%2==0:
    flag =True
else:
    flag = False
index = 0

for i in range(len(data)):
    
    if alpha == data[i]:
        index = i+1
        break
if index%2==0:
    if flag:
        print("BLACK")
    else:
        print("WHITE")
else:

    if flag:
        print("WHITE")
    else:
        print("BLACK")

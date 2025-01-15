s = input()


count = 0

mx = 0

for i in s:
    if i == "0":
        count+=1

    else:
        if mx <count:
            mx = count 
        count =0
if mx <count:
            mx = count 
        
print(mx)

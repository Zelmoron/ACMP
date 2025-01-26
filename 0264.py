n = int(input())


data = [int(i) for i in input().split()]

count = 0
mx = 0

for i in data:
    if i >0:
        count+=1
    
    else:
        if mx <= count:
            
            mx = count
        count = 0

if mx <= count:
            
    mx = count

print(mx)
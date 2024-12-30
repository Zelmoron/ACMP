# 1 1 
# 4 2
# 6 3
#10 4


n  = int(input())


count = 1
box = 0
mx = 0
for i in range(n):
    box +=1
    if box == count:
        box = 0
        mx = count
        count+=1
print(mx)
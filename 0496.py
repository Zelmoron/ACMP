n = int(input())

data = [int(i) for i in input().split()]


mx = 0


for i in range(-1,len(data)-1):
    sm = data[i-1]+data[i]+data[i+1]
    if sm > mx:
        mx = sm

print(mx)
n = int(input())


data = [int(i) for i in input().split()]


room = int(input())

count = 0

for i in data:
    if i-room >=0:
        count+=room
    else:
        count+=i
print(count)
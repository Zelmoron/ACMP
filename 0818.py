n = int(input())

data = [int(i) for i in input().split()]




for i in range(len(data)):
    data[i]-=1

print(sum(data)+1)

n = int(input())

data = []



for i in range(1,n+1):
   if n%i==0:
      data.append(i)
      


print(int(sum(data)))
n,i,j = map(int,input().split())

a = max(i,j)-min(i,j)-1
b = n-max(j,i)+min(i,j)-1
print(min(a,b))

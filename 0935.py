data = [int(i) for i in input().split()]


n = abs(data[1]-data[0])
m= abs(data[3]-data[2])


print("YES" if n%2==m%2 else "NO")
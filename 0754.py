data = [int(i) for i in input().split()]


mn,mx = min(data),max(data)

if mn < 94 or mx > 727:
    print("Error")
else:
    print(mx)
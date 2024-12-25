data = [int(i) for i in input().split()]

data.sort()

print("YES" if data[0]+data[1] >data[2] else "NO")

data = [int(i) for i in input().split()]

x1, y1 = data[0], data[1]
x2, y2 = data[2], data[3]
x3, y3 = data[4], data[5]

area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

print(area)

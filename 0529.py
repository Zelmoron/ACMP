import math

def calculate_segment_length(x1, y1, x2, y2):
    length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return length

   
data = [int(i) for i in input().split()]


x1,y1 = data[0],data[1]
x2,y2 = data[2],data[3]


length = calculate_segment_length(x1, y1, x2, y2)


print(f"{length:.10f}")

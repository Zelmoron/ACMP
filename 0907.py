data = [int(i) for i in input().split()]

import math

print("YES" if min(data[0],data[1]) >= 2*data[-1] else "NO")
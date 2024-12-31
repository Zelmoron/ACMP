import math

n = int(input())


k = math.ceil(n / 6)

min_score = 7 * k - n


print(min_score, n*6)

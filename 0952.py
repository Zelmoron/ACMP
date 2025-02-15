
a, b = map(int, input().split())

if a == 0 and b > 0:
	print("Impossible")
else:

	min_cost = max(a, b) if b <= a else a + (b - a)
	max_cost = a + max(0, b - 1)

	print(min_cost, max_cost)

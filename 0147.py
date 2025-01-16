n = int(input())
#0 1 1 2 3 5 8 13

pr = 0

r = 1
for i in range(n):
    m = r
    r = pr + r
    
    pr = m

print(pr)

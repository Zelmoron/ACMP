n = int(input())



data = [int(i) for i in input().split()]


result1 = []
result2 = []
for i in data:
    if i%2==0:
        result1.append(i)
    else:
        result2.append(i)


print(*result2)
print(*result1)


print("YES" if len(result1)>=len(result2) else "NO")
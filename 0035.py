n = int(input())


result = []
for i in range(n):

    data = [int(i) for i in input().split()]

    n = data[0]
    m = data[1]
    result.append(int(19*m + (n + 239)*(n + 366) / 2))


print(*result,sep="\n")
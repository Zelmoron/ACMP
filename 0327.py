n = int(input())


def check(data):
    return sum(map(int,str(data)[:-3])) == sum(map(int,str(data)[-3:]))



for i in range(n):
    a = int(input())
    print("Yes" if check(a+1) or check(a-1) else "No")
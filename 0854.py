a,b = map(int,input().split())

s = input()




match s:
    case "heat":
        print(b if b>a else a)
    case "freeze":
        print(b if b<a else a)

    case "auto":
        print(b)

    case "fan":
        print(a)
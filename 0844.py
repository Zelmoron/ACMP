a,b = map(int,input().split())

result = (a*b)**0.5
print(int(result) if int(result)-result == 0.0 else 0 )
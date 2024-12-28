n = int(input())


s = str(n).zfill(4)
if n %400==0 or (n%4==0 and n%100!=0):
    print("12/09/"+s)
else:
    print("13/09/"+s)
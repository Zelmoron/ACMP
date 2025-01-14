

data = "AEBMKPOTYXHC"
n = int(input())
def main():
    s = input()


    ln = len(s)

    if ln != 6:
        print("No")
        return

    sr =s[1:4]

    sr2 = s[0:1]+s[4:]

    if sr.isdigit():
        pass
    else:
        print("No")
        return
    
    count = 0
    
    for i in sr2:
        if i in data:
            count+=1
        
    print("Yes" if count ==3 else "No")


for i in range(n):
    main()